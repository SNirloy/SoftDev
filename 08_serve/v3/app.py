# James, Nada, Sadi of Soup Sharks
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #Printed on the terminal
    return "No hablo queso!"

app.debug = True #Prints debug code in the terminal
app.run()

"""
The following statements appeared in the terminal before the printed statements:

 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 642-084-393

This debugger pin is the same for everytime this is run.
What is the significance of this?

There are different line printed in thonny:

 * Restarting with stat
/usr/bin/python3: No module named thonny.plugins.cpython.app

I guess thonny is not capable of handling flask.DEBUG, at least on the default version.
"""