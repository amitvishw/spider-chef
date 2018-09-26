from flask import Flask

__version__ = "0.1"

app = Flask('SpiderChef')
app.debug = True
app.config['SECRET_KEY'] = ''

from src.controllers.controllers import *
