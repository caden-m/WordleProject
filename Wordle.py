# File: Wordle.py

"""
PM: Caden Marquis 
SCRUM Master: Matthew McCord 
SCRUM Team: Brittany Choi, Taylor Anderson, Stefany Guevara

"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    word = random.choice(FIVE_LETTER_WORDS)

    # I do not know what to call the input word and my mac won't run the program.. 
    # so may have to test it on monday with everyone --Brittany
    def enter_action(s):
        # g = 0 
        # for i in s:
        #     gw.set_square_letter(0, g, i)
        #     c+= 1
        #     print(i,g)

        s.lower()
        if s in FIVE_LETTER_WORDS:
            gw.show_message("Great guess!")
        else:
            gw.show_message("Not in word list.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    c = 0 
    for i in word:
        gw.set_square_letter(0, c, i)
        c+= 1
        print(i,c)

# Startup code

if __name__ == "__main__":
    wordle()



