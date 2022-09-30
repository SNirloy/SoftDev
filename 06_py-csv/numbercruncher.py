"""
Pamus: Mahir Riki, Sadi Nirloy
K06: StI/O: Divine your Destiny!
"""

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
print (occupations)