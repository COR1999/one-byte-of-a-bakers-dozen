import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint, session
from werkzeug.security import generate_password_hash, check_password_hash
from views.db import mongo

login_user = Blueprint('login_user', __name__)


@login_user.route("/login", methods=["GET", "POST"])
def login():
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
    recipe = mongo.db.recipe_project.find({"author": fullName})
    checkedPW = check_password_hash(dbPassword, password)
    session["user_name"] = fullName
    if len(list(recipe)) == 0:
        return redirect(url_for("load_many_recipes.load_recipes"))

    if email == dbEmail and checkedPW:
        return redirect(url_for("load_many_recipes.load_recipes"))
    else:
        return redirect(url_for("load_many_recipes.load_recipes"))
