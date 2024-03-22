# Author: Ethan Newman
# Description: Basic Logic for the Hangman game, includes play_game, guess_letter, check_game, and print_word.
# Utilizes Random library in main to random generate a word, which is then passed in as r_word.


class Hangman:

    def __init__(self, RandomWord):
        self.r_word = RandomWord
        self.num_guesses = 6
        self.curr_guess = 0
        self.letters = []

    #Checks whether the guessed letter is correct or not, then adds that letter to the guessed letter list.

    def guess_letter(self, l):

        if l in self.r_word:
            self.letters.append(l)
            return True

        elif l not in self.r_word:
            self.letters.append(l)
            self.curr_guess = self.curr_guess + 1
            return False

    #Prints the current word generated after guessing letters.

    def print_word(self):
        i = 0
        temp_word = []
        for x in self.r_word:
            temp_word.append('_')

        for x in self.letters:
            while i < len(self.r_word):
                if x == self.r_word[i]:
                    temp_word[i] = x
                    i = i + 1
                else:
                    i = i + 1
            i = 0
        return ''.join(temp_word).capitalize()

    #Gets the remaining number of guesses.

    def get_tries(self):
            return self.num_guesses

    #Gets the current guess it is on.

    def get_curr(self):
            return self.curr_guess

    #Gets the list of letters used.

    def get_letter_list(self):
        return self.letters

    #Gets the word as it is checked.

    def get_word(self):
        return self.r_word
