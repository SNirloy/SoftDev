import random

with open('krewes.txt', 'r') as f:
    lines = f.readline()
krewes_list = lines.split("@@@")

krewes = {}
          
for i in krewes_list:
    person = i.split("$$$")
    pdNum = int(person[0])
    if (not pdNum in krewes.keys()):
        krewes[pdNum] = []
    list = [person[1], person[2]]
    krewes[pdNum].append(list)

def random_devo():
# printing both the devo's name, period, and ducky
# list is bugging out, so we need this roundabout way of 
    counter = 0
    period = -1
    index = random.randrange(0, len(krewes.keys()))
    for i in krewes.keys():
        if (counter == index):
            period = i
        counter += 1
    person_and_ducky = random.choice(krewes[period])
    name = person_and_ducky[0]
    ducky = person_and_ducky[1]
    print("Period " + str(period) + ": " + name + " ft. " + ducky)


random_devo()
