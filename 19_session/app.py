"""

"""
from flask import Flask
from flask import session
from flask import render_template
from flask import request
from flask import redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)


logins = {
    "gastric bypass train": "Heebiejeebies"
}

@app.route("/")
def login_page():
    print(request.form)
    return render_template("login.html")

@app.route("/response", methods = ["POST", "GET"])
def response():
    if(request.method == "POST"):
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
    elif(request.method == "GET"):
        session["username"] = request.args["username"]
        session["password"] = request.args["password"]

    if(not session["username"] in logins.keys()):
      return "<h1>Who are you? I have no recollection of a " + str(session["username"]) + ".</h1>"
    if (not logins[session["username"]] == session["password"]):
      return "<h1> Not the right password. SOUND THE INTRUDER ALERT!!!</h1>"
    return render_template("response.html", username = session["username"])

@app.route("/logout")
def logout():
  session.pop("username")
  session.pop("password")
  print(session)
  return render_template("login.html")

app.Debug = True
app.run()