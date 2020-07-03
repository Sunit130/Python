from flask import Flask, render_template, redirect, url_for, request
import datetime, random

app = Flask(__name__)

my_guess = random.randrange(100)
content = []

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        print("entered")
        number = int(request.form["number"])
        if number == my_guess:
            content.append("Conratulations!!")
        elif number > my_guess:
            content.append("You guessed greater!!")
        else:
            content.append("You guessed lesser!!")

    return render_template("index.html", content = content)
