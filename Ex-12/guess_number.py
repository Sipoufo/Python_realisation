from art import logo 
import random

print("Welcome to the Number Guessing Game")

# init
live = 0
run = True

# function
def add_live(difficulty):
    if difficulty.lower() == 'easy':
        return 10
    elif difficulty.lower() == 'hard':
        return 5

def compare(user, rand):
    if user < rand:
        print("Too low")
    elif user > rand:
        print("Too high")
    else:
        print(f"You got it! the answere was {guess}")
        
    
# running the app
while run:
    print(logo)
    print("I'm thinking of a number between 1 and 100: ")
    answere = random.randint(1, 101)
    print(f"Pssf {answere}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    live = add_live(difficulty)
    guess = 0
    while guess != answere:
        if live == 0:
            print(compare(guess, answere))
            print("You've run out of guesses, you lose")
            run = False
            break
        elif guess == answere:
            compare(guess, answere)
            run = False
        else:
            print(f"You have {live} attempts remaning to guess the number")
            guess = int(input("Make a guess: "))
            live -= 1
            compare(guess, answere)
            print("Guess again")
    
    again = input("Try again? 'Yes' or 'No': ")
    if again == 'No':
        run = False
    else:
        run = True
    
    
