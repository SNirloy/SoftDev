"""

"""
from flask import Flask
from flask import session
from flask import render_template
from flask import request
from flask import redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)


logins = {
    "gastric bypass train": "Heebiejeebies"
}
"""
@app.route("/", methods = ["POST", "GET"])
def login_page():
    print(len(request.form))
    print(len(request.args))
    if(len(request.form) == 0 and len(request.args) == 0):
      return render_template("login.html")
    print(request.form)
    print(request.args)
    return render_template("login.html")
"""

@app.route("/", methods = ["POST", "GET"])
def home_page():
    print(len(request.form))
    print(len(request.args))
    print(session)
    print(request.form)
    print(request.args)
    if(len(request.form) > 0):
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
    if(len(request.args) > 0):
        session["username"] = request.args["username"]
        session["password"] = request.args["password"]
    if(len(session) > 0):
      if(not session["username"] in logins.keys()):
        return "<h1>Who are you? I have no recollection of a " + str(session["username"]) + ".</h1>"
      if (not logins[session["username"]] == session["password"]):
        return "<h1> Not the right password. SOUND THE INTRUDER ALERT!!!</h1>"
      return render_template("response.html", username = session["username"])
    return render_template("login.html")

@app.route("/logout")
def logout():
  session.pop("username")
  session.pop("password")
  print(session)
  return redirect("/")

if __name__ == "__main__":
  app.debug = True
  app.run()