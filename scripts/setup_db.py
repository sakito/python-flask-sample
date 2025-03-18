#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
from api_rest.app import db


def main():
    """
    起動
    """
    db.create_all()

if __name__ == '__main__':
    main()
