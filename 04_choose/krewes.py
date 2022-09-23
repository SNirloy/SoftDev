"""
Emily Ortiz, Sadi Narloy, Ravindra Mangar
SoftDev
TNPG: Wasabi Rain
2022-09-22
"""

import random

def get_rand_num():
  return random.randrange(3)

list = [2, 7, 8]

#FOR LOOP TO VERIFY THAT RESULTS ARE RANDOM // RUNS TEN TIMES
for i in range(10):

  krewes = {2:["Anson", "Efe", "Faiza"], 7:["Ravindra", "Emily", "Sadi"], 8:["Sasha", "Shreya", "Jeffery"]}

  #print((krewes[list[get_rand_num()]])[get_rand_num()])
  period_list = krewes[list[get_rand_num()]]
  person = period_list[get_rand_num()]
  print(person)

