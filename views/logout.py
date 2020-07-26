import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
# import uuid
# import configparser
from views.db import mongo


# from run import mongo
# from loadManyRecipes import loadManyRecipes

# from run import mongo
# from run import app, mongo
logout_user = Blueprint('logout_user', __name__)


@logout_user.route("/logout")
def logout():
    session["user_name"] = ""
    print("hello")
    return redirect(url_for("load_many_recipes.load_recipes"))


# @login_user_example.route("/login_to", methods=["GET"])
# def login_user():
#     session["user_id"] = 1
#     return render_template("loadManyRecipes.html")
