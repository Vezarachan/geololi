# -*- coding: utf-8 -*-
"""
- model module 数据模型模块
- This module includes data models required.

:author Lou Xiayin
:date 2019/12/31
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()