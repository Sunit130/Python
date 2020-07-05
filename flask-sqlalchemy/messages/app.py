from flask import Flask, request, render_template, redirect, flash, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import re

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

engine = create_engine("postgresql://postgres:root@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    if not session.get("username"):
        return render_template("login.html")
    else:
        messages=db.execute("SELECT * from messages").fetchall()
        return render_template("index.html", messages=messages)



@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    count = db.execute("SELECT COUNT(*) from users WHERE username=:username AND password=:password", {"username":username, "password":password}).fetchall()[0][0]
    if count == 1:
        session["username"] = username;
        return("entered")
    else:
        return("fail")



@app.route("/add", methods=["POST"])
def add():
    message = request.form["message"]
    db.execute("INSERT INTO messages(username, message) VALUES (:username, :message)", {"username":session["username"], "message":message})
    db.commit()
    return redirect("/")



@app.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    if not session.get("username"):
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        message = request.form["message"]
        message = db.execute("UPDATE messages SET username= :username, message= :message WHERE id= :id",
                                {"msessage":message,"username":username,"id":id})
        db.commit()
        return redirect("/")
    else:
        message = db.execute("SELECT * from messages WHERE id=:id", {"id":id}).fetchall()
        return render_template("update.html", message=message)


@app.route("/delete/<id>")
def delete(id):
    if not session.get("username"):
        return render_template("login.html")
    try:
        db.execute("DELETE FROM messages WHERE id=:id", {"id":id})
        db.commit()
        return "Message DELETED"
    except:
        return "not found"


if __name__ == "__main__":
    app.debug = True
    app.run()
