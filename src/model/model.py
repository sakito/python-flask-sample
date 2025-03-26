#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
import sqlalchemy as db
from model.database import Base


class VuResult(Base):
    """
    脆弱性DB情報保存
    """
    __tablename__ = 'vuresult'

    uid = db.Column(db.String, primary_key=True)
    year = db.Column(db.String)
    value = db.Column(db.Unicode)
