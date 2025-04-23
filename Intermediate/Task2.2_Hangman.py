import random

def get_word_and_hint():
    words_with_hints = {
        "python": "A popular programming language.",
        "hangman": "A game where you guess letters to find a word.",
        "computer": "An electronic device for storing and processing data.",
        "programming": "The process of writing code to create software.",
        "developer": "A person who creates software applications.",
        "shadowfox": "An internship company."
    }
    word, hint = random.choice(list(words_with_hints.items()))
    return word, hint

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |
           |
           |
        """,
        """
           -----
           |   |
           |
           |
           |
           |
        """,
        """
           -----
           |
           |
           |
           |
           |
        """
    ]
    return stages[tries]

def play_hangman():
    word, hint = get_word_and_hint()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print(f"Hint: {hint}")
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please try again.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()