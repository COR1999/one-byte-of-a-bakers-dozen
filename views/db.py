import os
from flask_pymongo import PyMongo
from flask import Flask
from env import *

# if os.path.exists("env.py"):
#     import env

# x = os.getenv("MONGO_URI")
# print(x)


def create_app(app):
    # app = Flask(__name__, instance_relative_config=True)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    mongo = PyMongo(app)
    mongo.init_app(app)
    return mongo


# create_app()
