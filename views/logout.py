import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint, session
from views.db import mongo

logout_user = Blueprint('logout_user', __name__)


@logout_user.route("/logout")
def logout():
    session["user_name"] = ""
    return redirect(url_for("load_many_recipes.load_recipes"))
