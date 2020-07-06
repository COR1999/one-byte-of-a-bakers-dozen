import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import configparser
from flask import Blueprint
from views.db import *
from views.loadManyRecipes import *
from views.register import *
from views.createRecipe import *
from views.recipeDetails import *
# from views.env import *


app = Flask(__name__, instance_relative_config=True)
mongo = create_app(app)


@app.route("/")
def index():
    return loadManyRecipes(mongo)


@app.route("/addRecipe")
def addRecipe():
    return render_template("addRecipe.html")


@app.route("/registerUser", methods=["POST"])
def registerUser():
    register(mongo)
    return loadManyRecipes(mongo)


# @app.route("/loadRecipe/<recipeName>")
# def loadRecipe(recipeName):
#     return load_recipe(mongo, recipeName)


@app.route("/createRecipe", methods=["POST"])
def createRecipe():
    create(mongo, request)
    return loadManyRecipes(mongo)


@app.route("/showImage/<filename>")
def showImage(filename):
    return mongo.send_file(filename)


@app.route("/recipeDetails/<recipeName>")
def recipeDetails(recipeName):
    return recipe_Details(mongo, recipeName)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)
