print("Welcom to the Love Calculator")

name1 = input("What is your name ?")
name2 = input("What is their name ?")

name1_lowerCase = name1.lower()
name2_lowerCase = name2.lower()

name = name1 + " " + name2

TRUE = str(name.count('t') + name.count('r') + name.count('u') + name.count('e'))
LOVE = str(name.count('l') + name.count('o') + name.count('v') + name.count('e'))

love_Store = int(TRUE + LOVE)

if love_Store < 10 or love_Store > 90:
    print(f"Your score is {love_Store}, you go together like coke and mentos")
elif 40 < love_Store < 50:
    print(f"Your score is {love_Store}, you are already together")
else:
    print(f"Your score is {love_Store}")