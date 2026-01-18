import random

def get_guess():
    return input("Enter a letter: ")


def is_correct_guess(word, guess):
    if guess in word:
        return True
    else:
        return False

def update_display(word, guess, display):
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    return display

def is_not_correct_guess(attempts):
    attempts -= 1
    print(f"Incorrect! You have {attempts} attempts left.")
    return attempts

def fully_guessed(display):
    if "_" not in display:
        return True
    else:
        return False

def is_winner(display, word):
    if fully_guessed(display):
        return "You won!"
    else:
        return f"You lost! The word was: {word}"

def play_game():
    word = random.choice(['python', 'java', 'kotlin', 'javascript'])  # Example word list
    display = ['_' ]
    attempts = 6
    
    display = ['_'] * len(word)
    print("Welcome to Hangman!")
    print(" ".join(display))
    while attempts > 0:
        guess = get_guess()
        if is_correct_guess(word, guess):
            display = update_display(word, guess, display)
            print(" ".join(display))
            if fully_guessed(display):
                print(is_winner(display, word))
                break
        else:
            attempts = is_not_correct_guess(attempts)
    else:
        print(is_winner(display, word))
        
        
if __name__ == "__main__":
    play_game()