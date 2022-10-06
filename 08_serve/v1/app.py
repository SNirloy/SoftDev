# Nada, James, Sadi of Soup Sharks
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/home/students/2023/snirloy30/Documents/SoftDev/SoftDev/08_serve")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

"""
Predictions: We'll create a web page with the same message as last time \"No hablo queso!\", but there will be no print
statement in the terminal.

Works as expected

So we tried pasting our current directory in place of the \"/\", which led to the page becoming unable to load because it
could not find the url.
"""