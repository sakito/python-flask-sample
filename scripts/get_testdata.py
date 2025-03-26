#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
"""
サンプルを挙動させるためのデータを取得

このサンプルではNVDのデータを利用してみています
https://nvd.nist.gov/vuln/data-feeds#JSON_FEED

利用方法:
bin/py get_testdata.py
"""
import os
import urllib.request
import gzip
from pathlib import Path

import click

from sqlalchemy import select
from sqlalchemy.orm import aliased

from util import json_util
from model import model, database


@click.group(help='DBデータセットアップツール')

@click.pass_context
def cli(ctx: click.core.Context) -> None:
    pass


@cli.command(name='get', help='データ収集')
@click.option('--year', default='2024', help='年')
def get(year: str='2024') -> None:
    """
    データを取得する

    TODO 現在同じ名前のファイルは取得しない実装としているが、
         実際はこのデータは更新される事があるので、
         メタ情報を取得して上書き判定をする必要がある
    """

    # ファイル取得
    url = f'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-{year}.json.gz'

    # 保存ファイル位置
    file_name = os.path.basename(url)
    save_path = Path(f'data/nvd/{file_name}')
    if save_path.exists():

        print(f'exists: {save_path}')

    else:
        # ファイルが存在しない場合だけ保存
        with urllib.request.urlopen(url) as res:
            data = res.read()

        # ファイル保存
        save_path.parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, mode='wb') as f:
            f.write(data)

    file_path = f'data/nvd/nvdcve-1.1-{year}.json.gz'
    with gzip.open(file_path, 'rt', encoding='utf_8') as f:
        data = json_util.load_json(f.read())

        database.init_db()
        session = database.get_session()

        length = len(data['CVE_Items'])

        for idx, line in enumerate(data['CVE_Items']):
            uid = line['cve']['CVE_data_meta']['ID']

            result = model.VuResult(
                uid=uid,
                year=year,
                value=json_util.dump_json(line),
            )
            session.add(result)

            if idx > 0 and idx % 1000 == 0:
                print(f'{idx} / {length}')
                session.commit()

                # TODO 一旦1000件でテスト
                break

        session.commit()


@cli.command(name='build', help='データ変換')
@click.option('--year', default='2024', help='年')
def build(year: str='2024') -> None:
    """
    データを検索用に変換
    """
    session = database.get_session()

    vu = aliased(model.VuResult, name='vu')

    stmt = select(vu).where(vu.year==year).order_by(vu.uid)
    for row in session.execute(stmt):
        line = json_util.load_json(row.vu.value)

        print(line.keys())


if __name__ == '__main__':
    cli()
