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

from sqlalchemy import select
from sqlalchemy.orm import aliased

from util import json_util
from model import model, database


class Tool:
    """
    処理ツール
    """
    def dl_nvd(self, year='2024'):
        """
        nvdデータ取得
        """
        url = f'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-{year}.json.gz'
        file_name = os.path.basename(url)

        save_path = f'data/{file_name}'
        with urllib.request.urlopen(url) as res:
            data = res.read()

            # ファイル保存
            with open(save_path, mode='wb') as f:
                f.write(data)

    def save_db_nvd(self, year='2024'):
        """
        nvdデータを保存する
        """
        file_path = f'data/nvdcve-1.1-{year}.json.gz'
        with gzip.open(file_path, 'rt', encoding='utf_8') as f:
            data = json_util.load_json(f.read())

            database.init_db()
            session = database.get_session()

            length = len(data['CVE_Items'])

            for idx, line in enumerate(data['CVE_Items']):
                uid = line['cve']['CVE_data_meta']['ID']

                result = model.VuResult(
                    uid=uid,
                    value=json_util.dump_json(line),
                )
                session.add(result)

                if idx > 0 and idx % 1000 == 0:
                    print(f'{idx} / {length}')
                    session.commit()

                    # TODO 一旦1000件でテスト
                    break

            session.commit()

    def build_db_nvd(self, year='2024'):
        """
        nvdデータを検索用に変換
        """
        session = database.get_session()

        vu = aliased(model.VuResult, name='vu')

        stmt = select(vu).order_by(vu.uid)
        for row in session.execute(stmt):
            line = json_util.load_json(row.vu.value)

            print(line.keys())

    def run(self):
        """
        起動点
        """
        # self.dl_nvd()
        # self.save_db_nvd()
        self.build_db_nvd()


def main():
    """
    main
    """
    Tool().run()

if __name__ == '__main__':
    main()
