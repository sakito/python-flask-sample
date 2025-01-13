#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World! 確認用画面</p>'

