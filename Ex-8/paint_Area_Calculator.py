# import random
import math

def paint_calc(height, width, coverage):
    number_of_cans = math.ceil((height * width) / coverage)
    print(f"You'll need {number_of_cans} cans of paint")

h = int(input("Height of wall: "))
w = int(input("Width of wall: "))

# w = int(random.random())
# h = int(random.random())

coverage = 5

paint_calc(height=h, width=w, coverage=coverage)