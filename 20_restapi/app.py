import requests
from flask import render_template, Flask

app = Flask(__name__)

@app.route("/")
def home_page():
	response = requests.get("https://api.nasa.gov/planetary/apod?api_key=H3S4NkgQuewjgC8owP3DZIVgPmFdpgjhP0fSYgCa")
	dictionary = response.json()
	return dictionary

if __name__ == "__main__":
	app.debug = True
	app.run()