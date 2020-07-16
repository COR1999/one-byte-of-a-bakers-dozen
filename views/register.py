import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import configparser
from flask import Blueprint
# from
# from loadManyRecipes import *


register_user = Blueprint('register_user', __name__)


@register_user.route("/register_user", methods=["POST", "GET"])
def register(mongo):
    session["user_name"]
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
        # return loadManyRecipes(mongo)
