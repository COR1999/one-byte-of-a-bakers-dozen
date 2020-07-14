import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import configparser
# from run import *
from flask import Blueprint

# from run import *
load_recipe = Blueprint('load_recipe', __name__)


@load_recipe.route("/loadManyRecipes")
def load_many_recipes(mongo):
    all_recipes = mongo.db.recipe_project.find()
    list_of_recipes = list(all_recipes)

    print(list(all_recipes))

    return render_template("loadManyRecipes.html", recipeCollection=list_of_recipes)
