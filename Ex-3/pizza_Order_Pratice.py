print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want ? S, M, L: ")

if size == 'S':
    prise = 15
elif size == 'M':
    prise = 20
else:
    prise = 25

add_pepperoni = input("Do you want pepperoni ? Y or N; ")
if add_pepperoni == 'Y':
    if size == 'S':
        prise += 2
    elif size == 'M':
        prise += 3
    else:
        prise += 3
    extra_cheese = input("Do you want extra cheese ? Y or N; ")
    if extra_cheese == 'Y':
        if size == 'S':
            prise += 2
        elif size == 'M':
            prise += 3
        else:
            prise += 3

print(f"Your finally bill is: {prise}")