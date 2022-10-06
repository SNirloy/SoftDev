# James, Nada, Sadi of Soup Sharks
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablaron queso! <br> Tenemos hambre."

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
"""
Predictions:
    We know that __name__ == "__main__" so, app.debug will be true, and the run function will run.
    
Discos:
So, when the code is saved, the terminal prints a whole new set.
Furthermore, changes in the return statement can be seen upon reload.
We also saw that the printed statements are read as html, and not formatted from python. Ie) \n does not work. <br> was needed.
"""