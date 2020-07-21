
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
        author = request.form.get("author")
        if vegetarian == None:
            vegetarian = False
        # document_to_update = mongo.db.recipe_project.find_one({"recipeName": recipeName,
        #                                                        "author": author.lower()})
        # replacement_data = {"recipeName": recipeName,
        #                     "ingredients": ingredients,
        #                     "how_to": how_to,
        #                     "vegetarian": vegetarian,
        #                     "recipe_image_Id": randomFileName,
        #                     "author": author.lower()}
        # document_to_update.update({replacement_data})
        mongo.db.recipe_project.find_one_and_update(
            {"recipeName": recipeName, "author": author.lower()},
            {"$set": {"recipeName": recipeName,
                      "ingredients": ingredients,
                      "how_to": how_to,
                      "vegetarian": vegetarian,
                      "recipe_image_Id": randomFileName,
                      "author": author.lower()}}, upsert=False)

        return redirect(url_for("load_many_recipes.load_recipes"))


@edit_recipe.route("/edit_page/<recipeName>")
def load_edit_page(recipeName):
    recipe = mongo.db.recipe_project.find_one({"recipeName": recipeName})
    image = recipe["recipe_image_Id"]
    return render_template("edit_recipe.html",  recipe=recipe, image=image)
