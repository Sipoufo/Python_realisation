letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    final_word = ""
    for letter in text:
        if letter not in letters:
            final_word += letter
        else:
            position = letters.index(letter)
            if direction == "encode":
                new_position = position + shift
                if new_position <= 25:
                    final_word += letters[new_position]
                else:
                    final_word += letters[new_position - 26]
            elif direction == "decode":    
                new_position = position - shift
                print(new_position)
                if new_position >= 0:
                    final_word += letters[new_position]
                else:
                    final_word += letters[new_position + 26]
                
    print(f"{direction}d text is {final_word}")

restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if shift > 25:
        shift %= 25

    caesar(text, shift, direction)
    want_again = input("Type 'yes' if you want again , otherwise type 'no'\n")

    if want_again == 'no':
        restart = False
        print("Good Bye")