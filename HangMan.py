import random

def choose_word():
    superheroes = ['spiderman', 'batman', 'superman', 'ironman', 'wolverine', 'thor', 'hulk', 'captainamerica', 'blackwidow', 'flash']
    # Shuffle the list
    random.shuffle(superheroes)  
     # Select the first element after shuffling
    return superheroes[0] 

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the superhero name.")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        display = display_word(word, guessed_letters)
        print(display)

        if '_' not in display:
            print("Congratulations! You guessed the superhero name:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess.")
            attempts -= 1

    if attempts == 0:
        print("No more attempts. The superhero name was:", word)

if __name__ == "__main__":
    hangman()