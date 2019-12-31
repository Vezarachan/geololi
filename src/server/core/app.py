# -*- coding: utf-8 -*-
"""
- main module 主模块

:author Lou Xiayin
:date 2019/12/31

"""
from core import create_app
from flask import redirect, url_for, render_template

app = create_app()

@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"

# ------------ Routes ------------ #
@app.route("/")
def index():
    return redirect(url_for("playground"))


@app.route("/playground")
def playground():
    return render_template("base.html")


@app.errorhandler(404)
def page_not_found(code=None, info=None):
    return render_template("errors.html", code="404", info="page not found"), 404

