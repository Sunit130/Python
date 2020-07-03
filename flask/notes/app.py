from flask import Flask, render_template, request, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "This is SECRET_KEY"

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if not session.get("notes"):
            print("entered")
            session["notes"] = []
        print("Add")
        note = request.form["note"]
        session["notes"].append(note)
        return render_template("index.html", notes=session["notes"])
    else:
        if not session.get("notes"):
            return render_template("index.html", notes=None)
        else:
            return render_template("index.html", notes=session["notes"])
