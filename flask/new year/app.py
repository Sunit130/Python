from flask import Flask, render_template, redirect, url_for
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    result = now.month == 1 and now.day == 1
    return render_template("index.html", result=result)


app.run(debug=True)
