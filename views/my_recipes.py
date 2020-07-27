
import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint, session
# from flask_pymongo import PyMongo
# from bson.objectid import ObjectId
from views.db import mongo

my_recipes = Blueprint('my_recipes', __name__)


@my_recipes.route("/my_recipes/<author>")
def load_my_recipes(author):

    my_recipes = mongo.db.recipe_project.find({"Author": author})
    list_of_recipes = list(my_recipes)
    # image = recipe["recipe_image_Id"]
    return render_template("my_recipes.html",  recipeCollection=list_of_recipes)
