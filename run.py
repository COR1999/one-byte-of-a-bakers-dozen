import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import uuid
from array import array
from env import MONGO_URI

app = Flask(__name__)

# app.config["MONGO_DBNAME"] = ""
app.config["MONGO_URI"] = MONGO_URI


mongo = PyMongo(app)


class Recipe:
    def __init__(i, recipeName, ingredients, how_to, recipe_image_Id):
        i.recipeName = recipeName
        i.ingredients = ingredients
        i.how_to = [how_to]
        i.recipe_image_id = recipe_image_Id


@app.route("/")
def index():
    return redirect("loadManyRecipes")


@app.route("/addRecipe")
def addRecipe():
    return render_template("addRecipe.html")


@app.route("/loadRecipe/<recipeName>")
def loadRecipe(recipeName):
    name = mongo.db.recipe_project.find_one_or_404({"recipeName": recipeName})
    recipeObject = mongo.db.recipe_project.find_one(name)
    imageId = recipeObject["recipe_image_Id"]
    return render_template("showRecipe.html", recipeObject=recipeObject, image=imageId)


@app.route("/loadManyRecipes")
def loadManyRecipes():
    all_recipes = mongo.db.recipe_project.find()
    list_of_recipes = list(all_recipes)
    # row_length = 4
    # for i in range(0, len(all_recipes), row_length):

    print(list(all_recipes))

    return render_template("loadManyRecipes.html", recipeCollection=list_of_recipes)


@app.route("/createRecipe", methods=["POST", "GET"])
def createRecipe():
    if "recipe_image" in request.files:
        recipeImage = request.files["recipe_image"]
        randomFileName = str(uuid.uuid1()) + recipeImage.filename
        imageId = mongo.save_file(randomFileName, recipeImage)
        ingredients = request.form.get("ingredients").split("\n")
        how_to = request.form.get("how_to").split("\n")
        recipeName = request.form.get("recipeName")
        vegetarian = request.form.get("vegetarian")
        if vegetarian == None:
            vegetarian = False

        # print(vegetarian)
        mongo.db.recipe_project.insert_one(
            {"recipeName": recipeName,
             "ingredients": ingredients,
             "how_to": how_to,
             "vegetarian": vegetarian,
             "recipe_image_Id": randomFileName})
        return "done"

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
