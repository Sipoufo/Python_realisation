import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'w', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '/', '@', '²', '`', '^', 'µ', '!', '¨']

print("Welcome to the Pypassword Generator")
nr_letters = int(input("How many letters would you like in your password \n"))
nr_symbols = int(input(f"How many symbols woulds you like ?\n"))
nr_number = int(input(f"How many number woulds you like ?\n"))

# Easy
# password = ''
# for pass_letter in range(0, nr_letters):
#     password += random.choice(letters)

# for pass_symbol in range(0, nr_symbols):
#     password += random.choice(symbols)

# for pass_number in range(0, nr_number):
#     password += random.choice(numbers)

# print(password)

# Hard
password = []
password_final = ''
for pass_letter in range(0, nr_letters):
    password.append(random.choice(letters))

for pass_symbol in range(0, nr_symbols):
    password.append(random.choice(symbols))

for pass_number in range(0, nr_number):
    password.append(random.choice(numbers))

random.shuffle(password)
for p in password:
    password_final += p

print(password_final)  
