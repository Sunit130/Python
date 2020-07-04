from flask import Flask, request, render_template, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import re

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

engine = create_engine("postgresql://postgres:root@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    emails = db.execute("SELECT * from emails")
    return render_template("index.html", emails=emails)

@app.route("/add", methods=["POST"])
def add():
    email = request.form["email"]
    if not re.match("[a-zA-Z0-9-_]+(.[a-zA-Z0-9-_]+)*@[a-zA-Z0-9-]+([.a-zA-Z0-9]+)*(.[A-Za-z]{2,})", email):
        flash("NOT Valid EMAIL")
    else:
        flash("EMAIL added")
        db.execute("INSERT INTO emails (email, date) VALUES (:email, NOW())", {"email":email})
        db.commit()
    return redirect("/")


if __name__ == "__main__":
    app.debug = True
    app.run()
