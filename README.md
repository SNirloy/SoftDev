# Sadi Nirloy
## Workshop
### SoftDev 2022-2023
**Lab 11 Notes and Probably Review of Some of the Previous Labs**<br>
To make a form with Python:<br>
from flask import Flask, render_template, and request<br>
<ul>
  <li>Flask is an object that allows for serving websites</li>
  <li>render_template is a method that allows for the serving of html files that are stored in a folder called templates</li>
  <li>request is an object that holds a dictionary that stores the user's inputs of a website. This is linked to the HTML, and will be explained more later on.</li>
</ul>

```var = Flask(__name__)``` #to create the flask obj<br>
```@var.route("/")``` # to create a site at the root directory. A method that immediately follows this call will create a page with it's return<br>
Alternatively: ```@var.route("/", methods=['GET'])``` **or** ```@var.route("/", methods=['POST'])``` <br>
--Note that I have not been able to get methods=['POST'] to work. Must look at Piazza for more info
Afterwards: you can also do <br>
```@var.route("/<name>")``` to create other pages at different URLs, with the /*\<name\>* added to the base URL.<br>
<br>
**USING TEMPLATE**<br>
<ul>
<li>Have an HTML file in it</li>
<li>return render_template('fileName') in a method with an @var.route()</li>
</ul>
**USING STATIC**<br>
The file must be accessed through adding /static/file_name to the URL<br>
If it is not an html file, it will cause a download to occur
**REQUESTS and FORMS**<br>
In html, a form can be created like so:
```
<form action=<targetpage>
  <input type=fillin name=var>
  whatever else html you want 
  <input type="submit">
 </form>
```
The last input will create a button to be used to complete the form and bring you to the next page.
