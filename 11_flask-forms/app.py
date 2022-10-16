# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022
"""
James, Nada, Sadi of Soup Sharks
"""

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''



@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #This is the Flask's toString: it will probably contain the name and some other important information about the made site. However, since we ahve only chosen the name of the Flask instance, I do not know what else there might be inside the Flask object without looking at the documentation
    print("***DIAG: request obj ***")
    print(request) #Request is an object, but does not get instantiated anywhere. Is this something done by the Flask object? 
    print("***DIAG: request.args ***")
    print(request.args) #Request.args are most likely the user's inputs for the form.
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username']) #Should print the user's input for username, but this will be empty now, as there would be no input when the page was instantiated
    print("***DIAG: request.headers ***")
    print(request.headers) # Are these the holders of the user inputs?
    return render_template( 'login.html' )



"""
The link after submitting:
http://127.0.0.1:5000/auth?username=meep+merp&sub1=Submit

print(app) results (both times):
<Flask 'app'>

	It is a little odd how the variable name became the name of the instance. This is not a thing that happens with Java. Is this a python thing with __name__?

print(request) results ("/"):
<Request 'http://127.0.0.1:5000/' [GET]>

print(request) results ("/auth"):
<Request 'http://127.0.0.1:5000/auth?username=meep+merp&sub1=Submit' [GET]>

	It has the link/url and a way to get the inputs. We discussed get vs post, but where is this get decided? Is it a default of the request object. Also, why is it a list? Can every input be set to a different type of collection?
print(request.args) results ("/"):
ImmutableMultiDict([])

print(request.args) results ("/auth"):
ImmutableMultiDict([('username', 'meep merp'), ('sub1', 'Submit')])
	request.args is a dictionary with the keys of variables that have the user's inputs as the values


The difference between the two calls of print(request.headers) is the following line:
Referer: http://127.0.0.1:5000/
	which is the page before the new one is loaded

print(request.args['username'] in .route("/") results in:
an error: BadRequestKeyError
	Makes sense, since I saw that the dictionary was empty before pressing submit
	
print(request.args['username'] in .route("/auth") results in:
tester
	as expected
"""



@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])#Should print the string that the user had put in before they press Submit
    print("***DIAG: request.headers ***")
    print(request.headers)
    if(request.args['username'] == "testing"):
    	return "Waaaa hooo HAAAH"  #response to a form submission
    else:
      return "<img src=\"https://c.tenor.com/qTwpBu_N5SgAAAAC/quagsire-quagy-quagsire.gif\" style=\"height:500px;width:500px\">"



"""
When adding the argument methods=['GET', 'POST'] to both app.routes, nothing changes, at least not that I can see.
app.route("/", methods = ['POST']) causes an error
This appears in terminal 127.0.0.1 - - [16/Oct/2022 18:35:05] "GET / HTTP/1.1" 405
	The page results in a Method Not Allowed on the actual page
	404 error is the classic not found error, so what it 405?
The same thing happens when 'POST' is applied to the second app.route
"""



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
