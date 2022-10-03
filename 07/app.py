"""
Emily Ortiz, Sadi Nirloy, Ravindra Mangar (silenced) of Wasabi Rain
K07
"""

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0. 
1. Maybe it has relations to the forward slash in a url.
	Alternatively, the Terminal's directory are also separated by a forward slash.
2. 
3. 
4. This appears when you try to run the file with the python3 command or on thonny. We know because we tried it and got the following: 

* Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

When clicking on the link provided, we got the "No hablo queso!" message.
5. That looks like an invocation of a method, like in Java. 
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
