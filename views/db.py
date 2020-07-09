import os
from flask_pymongo import PyMongo
from flask import Flask, Blueprint
from views.env import *

createApp = Blueprint('createApp', __name__)


@createApp.route("/createApp")
def create_app(app):
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    mongo = PyMongo(app)
    # mongo.init_app(app)
    return mongo


# create_app(app)
