#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>

from flask import Flask

from ui.view import (
    # test はデバッグ、テンプレート用
    view_test,
)

app = Flask(__name__,
            static_url_path='/static',
            template_folder='template',
            static_folder='static')


# モジュール登録
PREFIX = '/ui'
app.register_blueprint(view_test.app, url_prefix=PREFIX)
# test は挙動確認用view

