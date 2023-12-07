import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _pick_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.list_of_guesses:
            print(f"You've already guessed '{guess}'. Try again.")
            return False

        self.list_of_guesses.append(guess)

        if guess in self.word.lower():
            print(f"Good guess! '{guess}' is in the word.")
            self._update_word_guessed(guess)
            return True
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. Lives remaining: {self.num_lives}")
            return False

    def _update_word_guessed(self, guess):
        for i in range(len(self.word)):
            if self.word[i].lower() == guess:
                self.word_guessed[i] = guess

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")

            if len(guess) == 1 and guess.isalpha():
                return guess.lower()
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

# Testing the Hangman class
hangman_game = Hangman(["Apples", "Bananas", "Cherries", "Grapes", "Kiwis"])

while True:
    user_guess = hangman_game.ask_for_input()
    if hangman_game.check_guess(user_guess):
        break
