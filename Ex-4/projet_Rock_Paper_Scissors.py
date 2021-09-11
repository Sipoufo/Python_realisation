import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

map = [rock, paper, scissors]

choose = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if 0 < choose < 3:
    print(map[choose])

    computerChoose = random.randint(0, len(map)-1)
    print(map[computerChoose])

    if (computerChoose == 0 and choose == 2) or (computerChoose == 2 and choose == 1) or (computerChoose == 1 and choose == 0):
        print("Computer win")
    elif computerChoose == choose:
        print("You are equal")
    else:
        print("You win")
else:
    print('Invalid choose')
