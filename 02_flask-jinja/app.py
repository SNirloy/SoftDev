# Soup Sharks: James, Sadi, Nada
# SoftDev
# Oct 2022


from flask import Flask, render_template #Q0: prediction: if we remove render_template, my_foist_template will just return no hablo queso
                                            #ACTUAL: we receive a NameError: "NameError: name 'render_template' is not defined"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: url prediction: ###/template/my_foist_template --> ACTUAL: 127.0.0.1:5000/my_foist_template (no /template)
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: render_template( template file, variable foo = "fooooo", list collection = coll)
    
if __name__ == "__main__":
    app.debug = True
    app.run()