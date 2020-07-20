import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import configparser
from flask import Blueprint
from views.db import mongo
from views.load_many_recipes import load_many_recipes
from views.login_user import login_user
from views.register import register_user
from views.create_recipe import create_recipe
from views.edit_recipe import edit_recipe

from views.recipe_details import recipe_details
# from views.login_user import login_user
# from views.db import createApp

if os.path.exists("views/env.py"):
    from views.env import *


app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = "random_string"
mongo.init_app(app)

# app.register_blueprint(create_app, url_prefix='/views')
app.register_blueprint(edit_recipe)
app.register_blueprint(create_recipe)
app.register_blueprint(load_many_recipes)
app.register_blueprint(recipe_details)
app.register_blueprint(login_user)
app.register_blueprint(register_user)


# @app.route("/addRecipe")
# def addRecipe():
#     return render_template("addRecipe.html")


# @app.route("/registerUser", methods=["POST"])
# def registerUser():
#     register(mongo)
#     return load_many_recipes(mongo)


# @app.route("/loadRecipe/<recipeName>")
# def loadRecipe(recipeName):
#     return load_recipe(mongo, recipeName)

# @app.route("/createRecipe", methods=["POST"])
# def createRecipe():
#     create(mongo, request)
#     return load_many_recipes(mongo)


# @app.route("/recipeDetails/<recipeName>")
# def recipeDetails(recipeName):
#     return recipe_details(mongo, recipeName)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)
