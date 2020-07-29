import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint, session
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from views.db import mongo

load_many_recipes = Blueprint('load_many_recipes', __name__)

@load_many_recipes.route("/")
def load_recipes():
    all_recipes = mongo.db.recipe_project.find()
    list_of_recipes = list(all_recipes)
    return render_template("load_many_recipes.html", recipeCollection=list_of_recipes)


@load_many_recipes.route("/showImage/<filename>")
def showImage(filename):
    return mongo.send_file(filename)
