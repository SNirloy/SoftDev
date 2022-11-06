"""

"""
from flask import Flask
from flask import session
from flask import render_template
from flask import request
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

logins = {
    "gastric bypass train": "Heebiejeebies"
}

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/response", methods = ["POST", "GET"])
def response():
    for i in request.form:
      session[i] = request.form[i]
    #print(session);
    #for i in session: 
    #  print(str(i) + ": " + str(session[i]))
    if (session["username"] in logins.keys() and logins[session["username"]] == session["password"]):
    	return render_template("response.html")
    return render_template("login.html") 

app.Debug = True
app.run()