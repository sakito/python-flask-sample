#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
"""
UI挙動確認用

http://<domain>/test で動作確認
"""
from flask import (
    Blueprint,
    render_template,
)

app = Blueprint(
    'views_test',
    __name__,
    template_folder='template',
    static_folder='static',
)


@app.route('/test')
def view_test():
    return '<p>Hello, World! 確認用画面</p>'

