# -*- coding: utf-8 -*-
"""
- manage module 管理模块
- This module includes common commands

:author Lou Xiayin
:date 2019/12/31
"""
from flask_script import Manager, Server
# from flask_migrate import Migrate
from core.app import app

manager = Manager(app)

# ---------- run server ---------- #
manager.add_command("runserver", Server())

# ------ database migrations ------#

if __name__ == "__main__":
    manager.run()
