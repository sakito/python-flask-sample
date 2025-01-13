#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
"""
gunicorn --config ui.py
"""

program_name = 'ui'

# debug用
# bind = ':8080'

# nginx用
bind = f'unix:var/run/sample_{program_name}.sock'

wsgi_app = f'{program_name}.app:app'
pidfile = f'var/run/{program_name}.pid'
pythonpath = '.'

workers = 3
threads = 3
timeout = 120
max_requests = 100
max_requests_jitter = 30

# end
