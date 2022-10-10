# James, Nada, Sadi of Soup Sharks
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # This is probably a constructor for Flask class
@app.route("/") # Something about a root directory & allows hello_world() to be flaskified
def hello_world():
    print(__name__) # Prints __main__ in the terminal when loaded and reloaded
    return "No hablo queso!"  #Prints the return statement on the web page

app.run()  # 
"""
When the app.run() is removed a new block of text in red appears in the shell/ terminal:
<<<<<<< HEAD
'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.
'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.
But the website still works.
Our best guess is tha the run method has some reference to a FLASK_DEBUG in it, but there is another default method
that is run without it.
"""
=======

'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.
'FLASK_ENV' is deprecated and will not be used in Flask 2.3. Use 'FLASK_DEBUG' instead.

But the website still works.
Our best guess is tha the run method has some reference to a FLASK_DEBUG in it, but there is another default method
that is run without it.
"""
>>>>>>> 4f7fb035e718d08d9243a815e326fb9d2fed379d
