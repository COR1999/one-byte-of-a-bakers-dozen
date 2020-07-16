
import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import configparser
# from run import *

from views.db import mongo

# from run import *

create_recipe = Blueprint('create_recipe', __name__)


@create_recipe.route("/create", methods=["POST", "GET"])
def create():
    if "recipe_image" in request.files:
        recipeImage = request.files["recipe_image"]
        randomFileName = str(uuid.uuid1()) + recipeImage.filename
        imageId = mongo.save_file(randomFileName, recipeImage)
        ingredients = request.form.get("ingredients").split("\n")
        how_to = request.form.get("how_to").split("\n")
        recipeName = request.form.get("recipeName")
        vegetarian = request.form.get("vegetarian")
        author = request.form.get("firstName")+" " + \
            request.form.get("lastName")
        if vegetarian == None:
            vegetarian = False
        mongo.db.recipe_project.insert_one(
            {"recipeName": recipeName,
             "ingredients": ingredients,
             "how_to": how_to,
             "vegetarian": vegetarian,
             "recipe_image_Id": randomFileName,
             "author": author.lower()})
        return redirect(url_for("load_many_recipes.load_recipes"))


@create_recipe.route("/create_page")
def load_create_page():
    return render_template("add_recipe.html")
