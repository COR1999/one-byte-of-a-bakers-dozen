import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# from run import *
from flask import Blueprint

# from run import *

recipe_details = Blueprint('recipe_details', __name__)


@recipe_details.route("/recipe_details/<recipeName>")
def recipe_details(mongo, recipeName):
    recipe = mongo.db.recipe_project.find_one({"recipeName": recipeName})
    image = recipe["recipe_image_Id"]
    return render_template("recipeDetails.html", recipe=recipe, image=image)
