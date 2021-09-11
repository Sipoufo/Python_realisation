import random

names_string = input("Give me everybody's names, separated by a comma \n")

names = names_string.split(", ")

random_Name = names[random.randint(0, len(names)-1)]

print(random_Name+"is going to buy the meal today !")