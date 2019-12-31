# -*- coding: utf-8 -*-
"""
- config module 配置文件
- This module contains dev/prod/test mode configuration for the application
* dev  - development mode
* prod - production mode
* test - testing mode

:author Lou Xiayin
:date 2019/12/30
"""

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = ""

class DevelopmentConfig(Config):
    DATABASE_URI = ""
    DEBUG = True

class TestingConfig(Config):
    DATABASE_URI = ""
    TESTING = True

CONFIG = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "test": TestingConfig,
    "default": DevelopmentConfig
}