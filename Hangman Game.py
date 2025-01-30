import random

def hangman():
    words = ['python', 'javascript', 'java', 'ruby', 'csharp']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")

    while attempts > 0 and '_' in guessed_word:
        print("\n" + ' '.join(guessed_word))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts -= 1

        guessed_letters.append(guess)

    if '_' not in guessed_word:
        print(f"Congratulations! You've guessed the word: {''.join(guessed_word)}")
    else:
        print(f"Game over! The word was: {word}")

hangman()
