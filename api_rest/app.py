#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>

import flask

from api_rest import (
    # test はデバッグ、テンプレート用
    api_test,
)


app = flask.Flask(__name__)

api_version = 'v1'
# モジュール登録

# test は挙動確認用
app.register_blueprint(api_test.app, url_prefix=f'/api/{api_version}')

