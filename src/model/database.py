#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from util import config_util


def get_db_path(key='result'):
    """
    DB位置を返す
    """
    root_dir = config_util.get_prj_root()
    db_path = root_dir / f'data/db/{key}.sqlite3'

    db_path.parent.mkdir(parents=True, exist_ok=True)

    return db_path


def get_engine():
    """
    engine取得
    """
    db_path = get_db_path()

    engine = create_engine(
        f'sqlite:///{db_path}',
        # echo=True,
    )

    return engine


def get_session():
    """
    セッション取得
    """
    engine = get_engine()
    session_factory = sessionmaker(
        autocommit=False,
        autoflush=True,
        bind=engine)

    session = scoped_session(session_factory)

    return session

Base = declarative_base()


def init_db():
    """
    DB初期設定
    """
    # すでにDBがある場合は削除する
    db_path = get_db_path()
    db_path.unlink(missing_ok=True)

    # DB初期生成
    engine = get_engine()
    Base.metadata.create_all(engine)
