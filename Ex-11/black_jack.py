import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = True

def current_score(list):
    score = 0
    for number in list:
        score += number
    return score

def compare_cards(user, computer):
    if (user > 21 and computer <= 21) or (user > 21 and computer > 21):
        print ("You lose")
    elif computer > 21 and user <= 21:
        print ("You win")
    else:
        if user > computer:
            print ("You win")
        elif user < computer:
            print ("You lose")
        else:
            if random.random() >= 0.5:
                print ("You win")
            else:
                print ("You lose")

def init() : 
    user_card['user']['cards'].append(cards[random.choice(cards)])
    user_card['user']['cards'].append(cards[random.choice(cards)])
    user_card['computer']['cards'].append(cards[random.choice(cards)])
    user_card['computer']['cards'].append(cards[random.choice(cards)])
    user_card['user']['score'] = current_score(user_card['user']['cards'])
    user_card['computer']['score'] = current_score(user_card['computer']['cards'])

def final_decision(user_card) :
    print(f"  Your final hand: {user_card['user']['cards']}, final score: {user_card['user']['score']}")
    print(f"  Computer's final hand: {user_card['computer']['cards']}, final score: {user_card['computer']['score']}")
    compare_cards(user_card['user']['score'], user_card['computer']['score'])

def another_card(gamer):
    user_card[gamer]['cards'].append(cards[random.choice(cards)])
    user_card[gamer]['score'] = current_score(user_card[gamer]['cards'])
            

while play:
    user_card = {
        'user': {
            "cards": [],
            "score": 0
        },
        'computer': {
            "cards": [],
            "score": 0
        }
    }
    play_black_jack = input("Do you want to play to play a game of black jack ? type: 'y' or 'n'")
    if play_black_jack == 'y':
        clear()
        print(logo)
        init()
        print(f"  Your cars: {user_card['user']['cards']}, current score: {current_score(user_card['user']['cards'])}")
        print(f"  Computer's first card: {user_card['computer']['cards'][0]}")
        if user_card['computer']['score'] < 17:
            if random.random() > 0.5:
                another_card('computer')
        another = input("Type 'y' to get another card, type 'n' to pass: ")
        if another == 'y':
            another_card('user')
            final_decision(user_card)
        elif another == 'n':
            final_decision(user_card)
    elif  play_black_jack == 'n':
        print("Good Bye")
        play = False