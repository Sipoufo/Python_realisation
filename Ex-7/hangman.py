import random
import hangman_words
import hangman_art

stages = hangman_art.stages
word_list = hangman_words.word_list
# random_word = word_list[random.randint(0, len(word_list)-1)]
# random choice
random_word = random.choice(word_list)
# lives
lives = len(stages) - 1
# initialization of then table of blanks
blanks = []

# logo
print(hangman_art.logo)

# Creation of table of blanks according to number of words to random word
for letter in random_word:
    blanks.append('_')

# print(f'Pssst, the solution is {random_word}.')

random_word_len = len(random_word)

# Start to the loop
loop = True
while loop:
    letter_guess = input("Guess a letter: ").lower()
    
    if letter_guess in blanks:
        print(f"You have already guess {letter_guess}")
            
    for s in range(0, random_word_len):
        # If guess is not a letter in the chosen_word
        # if letter_guess in blanks:
        #     print(f"You have already guess {letter_guess}")
        #     break 
        if letter_guess == random_word[s]:    
            blanks[s] = letter_guess
            # break 

    if letter_guess not in random_word:
        print(f"You guessed {letter_guess}, that's not in the word. You lose life")
        in_word = False
        lives -= 1
        if lives == 0:    
            print(f"The word is {random_word}")
            print('You lose')
            loop = False
        
    print(f"{' '.join(blanks)}")

    # print the stages
    print(stages[lives])
    
    # Check if user has got all letters.
    if not ('_' in blanks):
        loop = False
        print('You win')