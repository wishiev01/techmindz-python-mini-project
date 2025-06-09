#hangman

import random

words = ['python', 'hangman', 'programming', 'developer', 'keyboard', 'terminal']

def play_hangman():
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"You have {attempts} incorrect guesses allowed.")
    print("Word: " + ' '.join(guessed))

    while attempts > 0 and '_' in guessed:
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for i, char in enumerate(word):
                if char == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word. Attempts left: {attempts}")

        print("Word: " + ' '.join(guessed))

    if '_' not in guessed:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)

if __name__ == "__main__":
    play_hangman()
