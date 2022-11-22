"""
Table Corner: Thomas Zhang, Sadi Nirloy
Softdev
K20 -- A RESTful Journey Skyward: An introduction to Rest APIs
2022-11-22
time spent: 1.0 hr
"""
import requests
from flask import render_template, Flask

app = Flask(__name__)
api_key = ""
with open("key_nasa.txt") as api:
	api_key = api.readline().replace("\n", "")

@app.route("/")
def home_page():
	link = "https://api.nasa.gov/planetary/apod?api_key=" + api_key
	print("Key: " + link)
	response = requests.get(link)
	dictionary = response.json()
	return render_template("main.html", title = dictionary["title"], image = dictionary["url"], description = dictionary["explanation"])

if __name__ == "__main__":
	app.debug = True
	app.run()