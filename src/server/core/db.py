# -*- coding: utf-8 -*-
"""
- database module 数据操作模块
- This module is used for data access
* get_X    - get data
* add_X    - add data
* modify_X - modify data
* delete_X - delete data

:author Lou Xiayin
:date 2019/12/31
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

"""
# Create database instance
"""
# engine = create_engine("postgresql+psycopg2://user:password@host:port/dbname")
# db = scoped_session(sessionmaker(bind=engine))

"""
# data CRUD
"""
