import requests
import json
from flask import render_template, Flask

# location is a list/tuple with latitude and lognitude
def map_api(location):
    first_link = "http://dev.virtualearth.net/REST/V1/Imagery/Metadata/RoadOnDemand?output=json&include=ImageryProviders&key=AiPx2XExJSThPtl8ugxn9itZlnGFzSdAMvQl5DMSoJAOi5NoeBbLrCv3RFUDEIov"
    response = requests.get(first_link).json()
    for key in response.keys():
        print(str(key) + ": " + str(response[key]))
        print("")

# YOU CAN PLUG IN ANY VALUES YOU WANT SINCE IT IS JUST LAT LONG AND ZOOM

"""
app = Flask(__name__)

@app.route("/")
def home():
	return "GRHIFGHLFKDNB:LIJG"
app.run()
"""
map_api([1,1])