import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import uuid
from array import array

app = Flask(__name__)

# app.config["MONGO_DBNAME"] = ""
app.config["MONGO_URI"] = "mongodb+srv://cian:Greystones123@myfirstcluster-2axpy.mongodb.net/recipe-project?retryWrites=true&w=majority"


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
        mongo.db.recipe_project.insert_one(
            {"recipeName": recipeName,
             "ingredients": ingredients,
             "how_to": how_to,
             "recipe_image_Id": randomFileName})

    return redirect(url_for('loadRecipe', recipeName=recipeName))


@app.route("/showImage/<filename>")
def showImage(filename):
    return mongo.send_file(filename)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)
