"""

"""
from flask import Flask
from flask import session
from flask import render_template
from flask import request

app = Flask(__name__)
app.secret_key = b"help"

logins = {
    "gastric bypass train": "Heebiejeebies"
}

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/response", methods = ["POST", "GET"])
def response():
    session["username"] = request.form["username"]
    session["password"] = request.form["password"]
    
    username = request.cookies.get(session["username"])
    print(username)
    print(request.cookies)
    return render_template("response.html")

app.Debug = True
app.run()