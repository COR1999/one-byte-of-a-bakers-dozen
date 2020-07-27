import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint
from views.db import mongo


recipe_details = Blueprint('recipe_details', __name__)


@recipe_details.route("/recipe_details/<recipeName>")
def details_recipe(recipeName):
    recipe = mongo.db.recipe_project.find_one({"recipeName": recipeName})
    image = recipe["recipe_image_Id"]
    return render_template("recipe_details.html", recipe=recipe, image=image)
