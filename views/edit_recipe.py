
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

edit_recipe = Blueprint('edit_recipe', __name__)


@edit_recipe.route("/edit", methods=["POST", "GET"])
def edit():
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

        # replacement_data = {"recipeName": recipeName,
        #                     "ingredients": ingredients,
        #                     "how_to": how_to,
        #                     "vegetarian": vegetarian,
        #                     "recipe_image_Id": randomFileName,
        #                     "author": author.lower()}

        mongo.db.recipe_project.replaceOne(
            {"recipeName": recipeName, "author": author.lower()},
            {"recipeName": recipeName,
             "ingredients": ingredients,
             "how_to": how_to,
             "vegetarian": vegetarian,
             "recipe_image_Id": randomFileName,
             "author": author.lower()})

        return redirect(url_for("load_many_recipes.load_recipes"))


@edit_recipe.route("/edit_page")
def load_edit_page():
    return render_template("edit_recipe.html")
