import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint

load_recipe = Blueprint('load_recipe', __name__)


@load_recipe.route("/loadRecipe/<recipeName>")
def load_recipe(mongo, recipeName):
    name = mongo.db.recipe_project.find_one_or_404({"recipeName": recipeName})
    recipeObject = mongo.db.recipe_project.find_one(name)
    imageId = recipeObject["recipe_image_Id"]
    return render_template("showRecipe.html", recipeObject=recipeObject, image=imageId)
