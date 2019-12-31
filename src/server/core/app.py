# -*- coding: utf-8 -*-
"""
- main module 主模块

:author Lou Xiayin
:date 2019/12/31

"""
from core import create_app

app = create_app()

@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"

# ------------ Routes ------------ #