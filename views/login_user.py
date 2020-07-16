import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import configparser
# from run import *
from views.db import mongo


# from run import mongo
# from loadManyRecipes import loadManyRecipes

# from run import mongo
# from run import app, mongo
login_user = Blueprint('login_user', __name__)


@login_user.route("/login", methods=["GET", "POST"])
def login():
    # email = ""
    email = request.form.get("loginEmail_address")
    email.lower()
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
    session["user_name"] = firstName
    if len(list(recipe)) == 0:
        return redirect(url_for("load_many_recipes.load_recipes"))

    if email == dbEmail and checkedPW:
        return redirect(url_for("load_many_recipes.load_recipes"))
    else:
        return redirect(url_for("load_many_recipes.load_recipes"))


# @login_user_example.route("/login_to", methods=["GET"])
# def login_user():
#     session["user_id"] = 1
#     return render_template("loadManyRecipes.html")
