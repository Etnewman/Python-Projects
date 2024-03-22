# Author: Ethan Newman
# Description: Class for the GUI attached for Hangman

import tkinter
from Hangman import Hangman
from tkinter import *
from tkinter import font as fnt
from PIL import Image, ImageTk
import random

class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Hangman")
        self.photo_frame = Frame()
        self.start_button = Button()
        self.button_create = Button()
        self.button_random = Button()
        self.sub_button = Button()
        self.next_button = Button()
        self.text = Text()
        self.word = ''
        self.display_c = Label()
        self.display_i = Label()
        self.tries_label = Label()
        self.win = Label()
        self.lose = Label()

    #Startup of the game, generates the window and start button as well as main loop.

    def start_up(self):

        self.root.geometry('600x400')
        self.start_button = Button(self.root, text = "Start Game?!", command = lambda : self.generate_word(), font = fnt.Font(size = 30))
        self.start_button.place(x = 175, y = 150)
        self.root.mainloop()

    #Menu option for allowing the user to chose to create a word or generate one.

    def generate_word(self):

        self.start_button.destroy()
        self.button_create = Button(self.root, text = "Create Word", command = lambda : self.create_word(), font = fnt.Font(size = 20))
        self.button_random = Button(self.root, text = "Random Word", command = lambda : self.create_word_random(), font = fnt.Font(size = 20))
        self.button_create.place(x = 50, y = 150)
        self.button_random.place(x = 350, y = 150)
        
    #The actual start of the hangman game

    def start_game(self):
        self.next_button.destroy()

        self.image_list = self.get_images()
        self.hang.r_word = self.hang.get_word()
        self.root.geometry('800x800')
        self.image_list[0].place(x = 0, y = 0)
        intx = 75
        inty = 550
        self.button_list = self.create_buttons()
        self.display_word()
        self.display_num_tries()
        self.display_length = Label(self.root, text = "Length of word is: " + str(len(self.hang.r_word)), font = fnt.Font(size = 20))
        self.display_length.place(x = 500, y = 100)

        for button in self.button_list:
            button.place(x = intx, y = inty)
            intx = intx + 50

            if intx == 725:
                intx = 75
                inty = 650
            else:
                pass

    #Function that creates the Tkinter buttons, a-z.

    def create_buttons(self):
        buttons = []
        i = 0

        with open(r'C:\Users\ethan.newman\VSCode\Hangman\letters.txt', 'r') as r:
            letters = r.readlines()
            for x in range(0, 26):
                buttons.append(Button(self.root, text=letters[x], command = (lambda c = x, j = i:[self.press_button(letters[c].strip()), self.disable_button(j)]), font = fnt.Font(size = 10), justify = 'center', height = 5, width = 5))
                i = i + 1
            r.close()
        return buttons

    #This is the action for when a button is pressed, it checks the pressed button and determines whether or not it was correct and calls the functions accordingly.

    def press_button(self, l):

        check = self.hang.guess_letter(l)
        self.display_correct(check)
        guessed_letters = self.hang.get_letter_list()
        x = self.hang.get_curr()
        print(x)
        word = self.hang.print_word()
        self.image_list[x-1].destroy()
        self.image_list[x].place(x = 0, y = 0)
        self.display_label.destroy()
        self.display_word()
        self.display_num_tries()

        if x == 6:
            for button in self.button_list:
                button.configure(state= DISABLED)
            self.win_lose_label(False)

        elif word.lower() == self.word.lower() and x != 6:
            for button in self.button_list:
                button.configure(state= DISABLED)
            self.win_lose_label(True)

    #Gives the user the ability to create their own word.

    def create_word(self):
        self.button_create.destroy()
        self.button_random.destroy()
        self.text = Text(self.root, height = 6, width = 20, wrap = 'word')
        self.text.place(x = 250, y = 100)
        self.sub_button = Button(self.root, text = "Submit", command = lambda: self.get_data(), width = 22)
        self.sub_button.place(x = 250, y = 205)

    #Selects a random word from the Words.txt list.

    def create_word_random(self):
        self.button_create.destroy()
        self.button_random.destroy()

        with open(r'C:\Users\ethan.newman\VSCode\Hangman\Words.txt', 'r') as f:
            tdata = f.readlines()
            f.close()
            self.word = tdata[random.randint(0, (len(tdata)-1))].strip().lower()
            self.hang = Hangman(self.word)
            self.next_button = Button(self.root, text = "NEXT", command = lambda : self.start_game(), font = fnt.Font(size = 20))
            self.next_button.place(x = 250, y = 150)

    #Gets data from Textbox when entering a custom word.

    def get_data(self):
        self.word = self.text.get("1.0", "end-1c").lower()
        self.hang = Hangman(self.word)
        self.text.destroy()
        self.sub_button.destroy()
        self.next_button = Button(self.root, text = "NEXT", command = lambda : self.start_game(), font = fnt.Font(size = 20))
        self.next_button.place(x = 250, y = 150)

    #Gathers images from img_hangman

    def get_images(self):
        self.img0 = ImageTk.PhotoImage(Image.open(r'C:\Users\ethan.newman\VSCode\Hangman\img_hangman\img0.png'))
        self.lab0 = Label(self.root, image = self.img0)
        self.lab0.image = self.img0

        self.img1 = ImageTk.PhotoImage(Image.open(r'C:\Users\ethan.newman\VSCode\Hangman\img_hangman\img1.png'))
        self.lab1 = Label(self.root, image = self.img1)
        self.lab1.image = self.img1

        self.img2 = ImageTk.PhotoImage(Image.open(r'C:\Users\ethan.newman\VSCode\Hangman\img_hangman\img2.png'))
        self.lab2 = Label(self.root, image = self.img2)
        self.lab2.image = self.img2

        self.img3 = ImageTk.PhotoImage(Image.open(r'C:\Users\ethan.newman\VSCode\Hangman\img_hangman\img3.png'))
        self.lab3 = Label(self.root, image = self.img3)
        self.lab3.image = self.img3

        self.img4 = ImageTk.PhotoImage(Image.open(r'C:\Users\ethan.newman\VSCode\Hangman\img_hangman\img4.png'))
        self.lab4 = Label(self.root, image = self.img4)
        self.lab4.image = self.img4

        self.img5 = ImageTk.PhotoImage(Image.open(r'C:\Users\ethan.newman\VSCode\Hangman\img_hangman\img5.png'))
        self.lab5 = Label(self.root, image = self.img5)
        self.lab5.image = self.img5

        self.img6 = ImageTk.PhotoImage(Image.open(r'C:\Users\ethan.newman\VSCode\Hangman\img_hangman\img6.png'))
        self.lab6 = Label(self.root, image = self.img6)
        self.lab6.image = self.img6

        self.image_list = [self.lab0, self.lab1, self.lab2, self.lab3, self.lab4, self.lab5, self.lab6, self.lab0]
        return self.image_list

    #Disables button on press

    def disable_button(self, num):
        self.button_list[num].configure(state = DISABLED)

    #Dispays the word and updates it.

    def display_word(self):
        self.display_label = Label(self.root, text = self.hang.print_word(), font = fnt.Font(size = 20))
        self.display_label.place(x = 500, y = 150)

    #Destroys previous correct label and displays new one.

    def display_correct(self, check):
        self.display_c.destroy()
        self.display_i.destroy()

        if check:
            self.display_c = Label(self.root, text = "Correct!", font = fnt.Font(size = 20))
            self.display_c.place(x = 575, y = 225)
        else:
            self.display_i = Label(self.root, text = "Incorrect!", font = fnt.Font(size = 20))
            self.display_i.place(x = 575, y = 225)

    def display_num_tries(self):
        self.tries_label.destroy()
        x = self.hang.get_tries()
        self.tries_label = Label(self.root, text = "Number of Tries left: " + str(x - self.hang.get_curr()), font = fnt.Font(size = 20))
        self.tries_label.place(x = 500, y = 300)

    #Shows the ending frame, which displays if you won or not and destroys the previous frame.
    
    def win_lose_label(self, check):
        self.tries_label.destroy()
        self.display_label.destroy()
        self.next_button.destroy()
        self.display_c.destroy()
        self.display_i.destroy()
        self.display_length.destroy()

        self.root.geometry('600x400')

        for img in self.image_list:
            img.destroy()

        for button in self.button_list:
            button.place_forget()

        if check == True:
            self.win = Label(self.root, text = "You Win!!!", font = fnt.Font(size = 40))
            self.play_again = Button(self.root, text = "Play Again?", command = lambda :[self.restart(), self.start_up()], font = fnt.Font(size = 20))
            self.win.place(x = 200, y = 150)
            self.play_again.place(x = 235, y = 225)
        elif check == False:
            self.lose = Label(self.root, text = "You Lose!!!", font = fnt.Font(size = 40))
            self.play_again = Button(self.root, text = "Play Again?", command = lambda :[self.restart(), self.start_up()], font = fnt.Font(size = 20))
            actual_word = Label(self.root, text = "The word was: " + self.hang.r_word.capitalize(), font = fnt.Font(size = 20))
            self.lose.place(x = 175, y = 150)
            self.play_again.place(x = 210, y = 225)
            actual_word.place(x = 175, y = 25)

    def restart(self):
        self.root.destroy()
        self.root = Tk()
        self.display_c = Label()
        self.display_i = Label()
        self.tries_label = Label()
        self.win = Label()
        self.lose = Label()
