"""
Pamus: Mahir Riki, Sadi Nirloy
SoftDev
K06 - StI/O: Divine your Destiny!
2022-09-30
time spent: 1.2 hours
"""

"""
DISCO: 
- random.choices has a weighted parameter to it that randomly picks with probability
- The rsplit() python method could've done what our specialSplit(string) method did.
...
QCC:
- Are there any other way to efficiently turn a csv file into a dictionary?
...
HOW THIS SCRIPT WORKS:
- The file "occupations.csv" is read and put into a list.
- A for loop loops through this list to split the occupations up by commas and stores a list of lists into parsed_text.
- A for loop loops through parsed_text and makes the occupations into keys and percentages into values to the 
dictionary occupations.
- The function occupation_selector takes occupations and randomly selects an occupation with the percentages indicating the
probability of it being selected.
...
"""

import random as r

# used to split up each occupation with commmas in their name
def specialSplit(string):
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

reading = open("occupations.csv", "r") # opens "occupations.csv" and just reads it
list_of_all_text = reading.readlines() # turns each line of the csv file into a list 

# this makes another list that splits up the occupations correctly by ,
parsed_text = []
for i in list_of_all_text:
    parsed_text.append(specialSplit(i))

# to make the occupations dictionary
occupations = {}
for i in range(len(parsed_text)):
    job = parsed_text[i]
    if (i == 0):
        occupations[job[0]] = job[1]
    else:
        occupations[job[0]] = float(job[1])
occupations.pop('Job Class') # removes the job class key from the dictionary
occupations.pop('Total') # removes the total key from the dictionary
#print(occupations)

# function for weighted randomly selected occupations
def occupation_selector():
    percentages = list(occupations.values())
    occupation = r.choices(list(occupations.keys()), weights = percentages)
    return occupation[0]
    
print(occupation_selector())

# to print 15 occupations randomly weighted by percentages
# for i in range(15):
#    print(occupation_selector())

# To prove that our method of random choice is weighted
def proof(reps):
  #new dictionary to hold data
    randata = {}
  #To copy over the keys into Randata
    for i in occupations.keys():
        randata[i] = 0
    randata["Total"] = 0
  #Counting the number of times that each job is chosen
    for i in range(reps):
        randata[occupation_selector()] += 1
        randata["Total"] += 1
  #Calculating a percent for each job
    for i in randata.keys():
        percentAvg = (randata[i] / randata["Total"]) * 100
        if (not ( i == "Total")):
            print(str(i) + ": " + str(percentAvg) + " compared to " + str(occupations[i]))

print("\nAverage of Choices")
proof(1000000)
