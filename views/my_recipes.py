
import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint, session
from views.db import mongo

my_recipes = Blueprint('my_recipes', __name__)


@my_recipes.route("/my_recipes")
def load_my_recipes():
    print("ok!")
    my_recipes = mongo.db.recipe_project.find({"author": session["user_name"]})
    # {"Author": session["user_name"]}
    list_of_recipes = list(my_recipes)
    # image = recipe["recipe_image_Id"]
    print(session["user_name"])
    print(len(list_of_recipes))
    return render_template("my_recipes.html",  recipeCollection=list_of_recipes)
