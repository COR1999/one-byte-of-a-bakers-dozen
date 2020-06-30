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


register = Blueprint('register', __name__)


@register.route("/register", methods=["POST"])
def register(mongo):
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
