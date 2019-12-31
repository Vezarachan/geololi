# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
from flask import Flask
from config import CONFIG


def create_app(configuration=None):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    
    if configuration is None:
        app.config.from_object(CONFIG["dev"])
    
    return app
