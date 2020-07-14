import os
from flask_pymongo import PyMongo
from flask import Flask, Blueprint
# from views.env import *

if os.path.exists("views/env.py"):
    from views.env import *

create_app = Blueprint('create_app', __name__)


@create_app.route("/create_app")
def create_app(app):
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    mongo = PyMongo(app)
    mongo.init_app(app)
    return mongo


# create_app(app)
