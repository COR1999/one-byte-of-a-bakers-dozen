import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import configparser
from flask import Blueprint
from views.db import *
from views.env import *
from views.loadManyRecipes import *
from views.register import *
# from views.login_user import login_user
# from views.register import register
# from array import array

# if os.path.exists("views/env.py"):
#     import env

# x = os.getenv("MONGO_URI")
# print(x)

# app = create_app()
app = Flask(__name__, instance_relative_config=True)
mongo = create_app(app)
# app.register_blueprint(register)
# login_user = Blueprint('login_user', __name__)
# load_recipe = Blueprint('loadManyRecipes', __name__)

# app.register_blueprint(load_recipe)


@app.route("/")
def index():
    # return redirect("loadManyRecipes")
    return loadManyRecipes(mongo)


@app.route("/addRecipe")
def addRecipe():
    return render_template("addRecipe.html")


@app.route("/registerUser", methods=["POST"])
def registerUser():
    register(mongo)
    return loadManyRecipes(mongo)


@app.route("/loadRecipe/<recipeName>")
def loadRecipe(recipeName):
    name = mongo.db.recipe_project.find_one_or_404({"recipeName": recipeName})
    recipeObject = mongo.db.recipe_project.find_one(name)
    imageId = recipeObject["recipe_image_Id"]
    return render_template("showRecipe.html", recipeObject=recipeObject, image=imageId)


# @app.route("/loadManyRecipes")
# def loadManyRecipes():
#     all_recipes = mongo.db.recipe_project.find()
#     list_of_recipes = list(all_recipes)

#     print(list(all_recipes))

#     return render_template("loadManyRecipes.html", recipeCollection=list_of_recipes)


@app.route("/createRecipe", methods=["POST"])
def createRecipe():
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
        return redirect("loadManyRecipes")

# redirect(url_for('loadRecipe', recipeName=recipeName))


@app.route("/showImage/<filename>")
def showImage(filename):
    return mongo.send_file(filename)


@app.route("/recipeDetails/<recipeName>")
def recipeDetails(recipeName):
    recipe = mongo.db.recipe_project.find_one({"recipeName": recipeName})
    image = recipe["recipe_image_Id"]
    return render_template("recipeDetails.html", recipe=recipe, image=image)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)
