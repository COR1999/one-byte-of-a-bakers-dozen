import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import configparser
from run import *
from flask import Blueprint

from run import mongo
# from loadManyRecipes import loadManyRecipes

# from run import mongo
# from run import app, mongo


@login_user.route("/login", methods=["POST"])
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
