#Gastric Bypass Train - Sam Cowan, Anna Fang, Sadi Nirloy
#K14: Serving Looks
#SoftDev
#19-10-2022
#time spent: 0.7 hr

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def mimic():
	return render_template("index.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
