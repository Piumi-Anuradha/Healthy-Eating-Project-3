from flask import render_template
from taskmanager import app, db
from taskmanager import Category, Recipe


@app.route("/")
def home():
    return render_template("base.html")