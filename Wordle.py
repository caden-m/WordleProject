# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import enum
import random



from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, UNKNOWN_COLOR, WordleGWindow, N_COLS, N_ROWS

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
    
        for i, guessLetter in enumerate(Uguess):
            if Uguess[i] == Uactual[i]:
                WordleGWindow.set_square_color(gw, WordleGWindow.get_current_row(self), i, CORRECT_COLOR)
                Uactual = Uactual.replace(guessLetter, '-', 1)
            elif guessLetter in Uactual:
                WordleGWindow.set_square_color(gw, WordleGWindow.get_current_row(self), i, PRESENT_COLOR)
                Uactual = Uactual.replace(guessLetter, '-', 1)
            else:
                WordleGWindow.set_square_color(gw,WordleGWindow.get_current_row(self), i, MISSING_COLOR)


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

# def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
# def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
# def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))

guess = 'tttet'
Uguess = guess.lower()
print(Uguess)
UcharacterizedGuess = list(Uguess)
actual = 'tttan'
Uactual = actual.lower()
print(Uactual)
UcharacterizedActual = list(Uactual)

print(UcharacterizedGuess)
print(UcharacterizedActual)
row = 1
col = 0
color = UNKNOWN_COLOR
self = WordleGWindow()

for i, guessLetter in enumerate(Uguess):
    if Uguess[i] == Uactual[i]:
        WordleGWindow.set_square_color(self, WordleGWindow.get_current_row(self), i, CORRECT_COLOR)
        Uactual = Uactual.replace(guessLetter, '-', 1)
    elif guessLetter in Uactual:
        WordleGWindow.set_square_color(self, WordleGWindow.get_current_row(self), i, PRESENT_COLOR)
        Uactual = Uactual.replace(guessLetter, '-', 1)
    else:
        WordleGWindow.set_square_color(self,WordleGWindow.get_current_row(self), i, MISSING_COLOR)
    # if UcharacterizedGuess[i] == UcharacterizedActual[i]:
    #     prGreen(UcharacterizedGuess[i])
    #     WordleGWindow.set_square_color(WordleGWindow.get_current_row(), i, CORRECT_COLOR)
    # elif UcharacterizedGuess[i] in UcharacterizedActual:
    #     prYellow(UcharacterizedGuess[i])
    #     WordleGWindow.set_square_color(WordleGWindow.get_current_row(), i, PRESENT_COLOR)
    # else:
    #     prLightGray(UcharacterizedGuess[i])
    #     WordleGWindow.set_square_color(WordleGWindow.get_current_row(), i, MISSING_COLOR)

# CORRECT_COLOR = "#66BB66"       # Light green for correct letters
# PRESENT_COLOR = "#CCBB66"       # Brownish yellow for misplaced letters
# MISSING_COLOR = "#999999"       # Gray for letters that don't appear
# UNKNOWN_COLOR = "#FFFFFF"       # Undetermined letters are white
# KEY_COLOR = "#DDDDDD"           # Keys are colored light gray
