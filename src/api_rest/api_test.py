#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
"""
テスト用API
"""
import flask

app = flask.Blueprint(
    'api_test',
    __name__,
)

@app.route('/test')
def get_test():
    """
    表示テスト
    """
    response = 'テスト成功'
    return flask.jsonify(message=response)
