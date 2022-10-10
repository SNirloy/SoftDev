from flask import Flask

app = Flask(__name__)


import random

#dictionary with everything
krewes = {}
#lets read the file
file = open("occupations.csv")
#print(file.read())
text = file.read()
mrm = text.split("\n")
x = 0
for i in mrm:
    #x exists just bc there are random lns of info that shouldn't be generated
    x += 1
    if x in range(2,len(mrm)):
        if("," in i):
            #to deal with quotations
            if("\"" in i):
                #print("shoot")
                #print(i)
                quotes = i.split("\"")
                #print(quotes)
                perc = quotes[2]
                percc = perc[1:]
                krewes[quotes[1]] = float(percc)
            else:
                #no commas in job
                eachLn = i.split(",")
                # print("each LINE:")
                # print(eachLn)
                # print(i)
                krewes[eachLn[0]] = float(eachLn[1])
#print(krewes)

def chooseJob(krewes):
    percList = krewes.values()
    #print(percList)
    jobList = list(krewes)
    #print(jobList)
    return (random.choices(jobList, weights = (percList))[0])
@app.route("/")
def rand_job():
    return("Soup Sharks: James, Nada, Sadi <br>"+ str(chooseJob(krewes)) + \
                                                      "<br>" + str(krewes.keys())[11:len(str(krewes.keys()))-2])
app.debug = True
app.run()
    