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
print(parsed_text)

occupations = {}
for i in parsed_text:
    occupations[