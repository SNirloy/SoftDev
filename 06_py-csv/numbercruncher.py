"""
Pamus: Mahir Riki, Sadi Nirloy
K06: StI/O: Divine your Destiny!
"""
import random

def specialSplit(string): #To handle the quotation marks 
    splitted = []
    lastIndex = 0
    locked = False
    for i in range(len(string)):
        theChar = string[i]
        if (theChar == "\""):
            locked = not locked
        if (theChar == "," and (not locked)):
            splitted.append(string[lastIndex: i])
            lastIndex = i+1
    splitted.append(string[lastIndex:-1])
    return splitted

reading = open("occupations.csv", "r")
list_of_all_text = reading.readlines()
parsed_text = []
for i in list_of_all_text:
    parsed_text.append(specialSplit(i))


occupations = {}
for i in range(len(parsed_text)):
    job = parsed_text[i]
    if (i == 0):
        occupations[job[0]] = job[1]
    else:
        occupations[job[0]] = float(job[1])
#print (occupations)

def chooseRandomWeighted():
    viable_keys = list(occupations.keys())
    viable_keys = viable_keys[1: len(viable_keys) - 1]
    viable_weights = list(occupations.values())
    viable_weights = viable_weights[1: len(viable_weights) - 1]
    choice = random.choices(viable_keys, viable_weights, k = 1)
    return choice[0]

print(chooseRandomWeighted())

def proof(reps):
    randata = {}
    counter = 0
    for i in occupations.keys():
        if (counter > 0):
            randata[i] = 0
        counter += 1
    for i in range(reps):
        randata[chooseRandomWeighted()] += 1
        randata["Total"] += 1
    for i in randata.keys():
        percentAvg = (randata[i] / randata["Total"]) * 100
        print(str(i) + ": " + str(percentAvg) + " compared to " + str(occupations[i]))

print("\nAverage of Choices")
proof(1000000)
