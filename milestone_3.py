import random

word_list = ["Apples", "Bananas", "Cherries", "Grapes", "Kiwis"]

random_fruit = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()

    if guess in random_fruit.lower():
        print(f"Good guess! '{guess}' is in the word.")
        return True
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False

def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")

        if len(guess) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Testing the code
while True:
    user_guess = ask_for_input()
    if check_guess(user_guess):
        break
