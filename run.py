import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
# from array import array
from env import MONGO_URI

app = Flask(__name__)

# app.config["MONGO_DBNAME"] = ""
app.config["MONGO_URI"] = MONGO_URI


mongo = PyMongo(app)


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

    print(list(all_recipes))

    return render_template("loadManyRecipes.html", recipeCollection=list_of_recipes)


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


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("loginEmail_address").lower()
    password = request.form.get("loginPassword")
    user = mongo.db.users.find_one({"email_address": email})
    dbEmail = user["email_address"]
    dbPassword = user["password"]
    firstName = user["FirstName"]
    lastName = user["LastName"]
    fullName = firstName.lower() + " " + lastName.lower()
    all_recipes = mongo.db.recipe_project.find()
    list_of_recipes = list(all_recipes)
    print(fullName)
    recipe = mongo.db.recipe_project.find({"author": fullName})
    print(len(list(recipe)))
    checkedPW = check_password_hash(dbPassword, password)
    if len(list(recipe)) == 0:
        return redirect("loadManyRecipes")

    if email == dbEmail and checkedPW:
        return render_template("loadManyRecipes.html", recipeCollection=list(recipe))
    
    
    

@app.route("/registerUser", methods=["POST"])
def registerUser():
    fName = request.form.get("firstName").lower()
    lName = request.form.get("lastName").lower()
    email = request.form.get("email_address").lower()
    user_password = request.form.get("password")
    password_repeat = request.form.get("password-repeat")
    if user_password == password_repeat:
        password = generate_password_hash(user_password, method='sha256')
        mongo.db.users.insert_one(
            {"FirstName": fName,
             "LastName": lName,
             "email_address": email,
             "password": password})
        return redirect("loadManyRecipes")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)
