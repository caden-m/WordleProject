# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    word = random.choice(FIVE_LETTER_WORDS)

    # I do not know what to call the input word and my mac won't run the program.. 
    # so may have to test it on monday with everyone --Brittany
    def enter_action(s):
        __name__.lower()
        if __name__ in FIVE_LETTER_WORDS:
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
    
    
# Function for moving to next row
def moveToNextRow(gw):

    # Check current row
    row = gw.get_current_row() # row = 0
    
    # Make sure that current row is not last row
    if row != 5:

        # Look at each column
        for i in range(5):
            color = gw.get_square_color(row, i)
            
            # set current row as the next row    
            if color != CORRECT_COLOR:
                gw.set_current_row(row + 1)



#Congratulatory message for when wordle is guessed
    if __name__ == word:
        gw.show_message("Splendid!")



