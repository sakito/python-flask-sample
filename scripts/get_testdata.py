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
            for line in f:
                print(line)


    def run(self):
        """
        起動点
        """
        # self.dl_nvd()
        self.save_db_nvd()


def main():
    Tool().run()

if __name__ == '__main__':
    main()
