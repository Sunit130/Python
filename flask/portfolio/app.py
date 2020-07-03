from flask import Flask, render_template, redirect, url_for
import datetime

app = Flask(__name__)

my_projects = ["Project1", "Project2", "Project3", "Project4"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutme")
def about():
    return render_template("aboutme.html")

@app.route("/projects")
def projects():
    return render_template("projects.html", my_projects=my_projects)
