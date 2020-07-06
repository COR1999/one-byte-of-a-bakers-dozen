import os
from flask_pymongo import PyMongo
from flask import Flask, Blueprint
from env import *

# if os.path.exists("env.py"):
#     import env

MONGO_URI = os.getenv("MONGO_URI")
# print(MONGO_URI)

createApp = Blueprint('createApp', __name__)


@createApp.route("/createApp")
def create_app(app):
    print(os.getenv("MONGO_URI"))
    # app = Flask(__name__, instance_relative_config=True)
    app.config["MONGO_URI"] = MONGO_URI
    mongo = PyMongo(app)
    # mongo.init_app(app)
    return mongo


# create_app(app)
