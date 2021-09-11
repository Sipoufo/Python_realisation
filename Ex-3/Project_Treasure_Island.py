print("Welcome to Treasure Island.")
print("Your mission is find the treasure.")

Cross_Road = input("You're at a cross road. Where is an island in the middle of the lake. Type \"left\" or \"right\"")

if Cross_Road.lower() == 'left':
    middle_Lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a "
                        "boat. Type \"swim\" for swim cross ")
    if middle_Lake.lower() == 'wait':
        Island_Unharmed = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and "
            "one blue. Which colour do you choose ? ")
        if Island_Unharmed.lower() == 'yellow':
            print('You win !')
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")