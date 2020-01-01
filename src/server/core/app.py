# -*- coding: utf-8 -*-
"""
- main module 主模块
- route module 路由模块

:author Lou Xiayin
:date 2019/12/31
"""
from core import create_app
from flask import redirect, url_for, render_template

"""
Flask App Instance
"""
app = create_app()

@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"

# ------------ Routes ------------ #
## ----------- Main Pages ------------ ##
@app.route("/")
def index():
    return redirect(url_for("playground"))


@app.route("/playground")
def playground():
    return render_template("datamanager.html")


@app.route("/geoviz")
def geoviz():
    return render_template("geoviz.html")

## ----------- Error Handlers ------------ ##
@app.errorhandler(404)
def page_not_found(code=None, info=None):
    return render_template("errors.html", code="404", info="page not found"), 404

