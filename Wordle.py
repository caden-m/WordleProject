# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import enum
import random


from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, UNKNOWN_COLOR, WordleGWindow, N_COLS, N_ROWS

# def wordle():

#     def enter_action(s):
#         gw.show_message("You have to implement this method.")

#     gw = WordleGWindow()
#     gw.add_enter_listener(enter_action)

# # Startup code

# if __name__ == "__main__":
#     wordle()
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))

guess = 'mateo'
Uguess = guess.upper()
print(Uguess)
UcharacterizedGuess = list(Uguess)
actual = 'ehtan'
Uactual = actual.upper()
print(Uactual)
UcharacterizedActual = list(Uactual)

print(UcharacterizedGuess)
print(UcharacterizedActual)
row = 1
col = 0
color = UNKNOWN_COLOR

for i in range(5):
    if UcharacterizedGuess[i] == UcharacterizedActual[i]:
        prGreen(UcharacterizedGuess[i])
        def set_square_color(self, row, col, color):
            self._grid[1][i].set_color(CORRECT_COLOR)
    elif UcharacterizedGuess[i] in UcharacterizedActual:
        prYellow(UcharacterizedGuess[i])
        def set_square_color(self, row, col, color):
            self._grid[1][i].set_color(PRESENT_COLOR)
    else:
        prLightGray(UcharacterizedGuess[i])
        def set_square_color(self, row, col, color):
            self._grid[1][i].set_color(MISSING_COLOR)

# CORRECT_COLOR = "#66BB66"       # Light green for correct letters
# PRESENT_COLOR = "#CCBB66"       # Brownish yellow for misplaced letters
# MISSING_COLOR = "#999999"       # Gray for letters that don't appear
# UNKNOWN_COLOR = "#FFFFFF"       # Undetermined letters are white
# KEY_COLOR = "#DDDDDD"           # Keys are colored light gray
