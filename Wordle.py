# File: Wordle.py

"""
PM: Caden Marquis 
SCRUM Master: Matthew McCord 
SCRUM Team: Brittany Choi, Taylor Anderson, Stefany Guevara
"""

import enum
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, UNKNOWN_COLOR, WordleGWindow, N_COLS, N_ROWS

def wordle(ActualWord, gw):
    # row = gw.get_current_row()
    # while gameOver == False:
    def enter_action(s):
        s = s.lower()
        if s in FIVE_LETTER_WORDS:
            gw.show_message("Great guess! Keep trying.")
        else:
            gw.show_message("Not in word list.")

        word = ActualWord
        UcharacterizedGuess = list(s)
        UcharacterizedActual = list(word)

        print(UcharacterizedGuess)
        print(UcharacterizedActual)
        
        
        c = 0 
        for i in s:
            gw.set_square_letter(0, c, i)
            c+= 1
            print(i,c)


        for i, guessLetter in enumerate(s):
            if s[i] == word[i]:
                WordleGWindow.set_square_color(gw, WordleGWindow.get_current_row(gw), i, CORRECT_COLOR)
                word = word.replace(guessLetter, '-', 1)
            elif guessLetter in word:
                WordleGWindow.set_square_color(gw, WordleGWindow.get_current_row(gw), i, PRESENT_COLOR)
                word = word.replace(guessLetter, '-', 1)
            else:
                WordleGWindow.set_square_color(gw,WordleGWindow.get_current_row(gw), i, MISSING_COLOR)

        
        # row = row + 1
        # print(row)
        # gw.set_current_row(row)

    gw.add_enter_listener(enter_action)



if __name__ == "__main__":
    ActualWord = random.choice(FIVE_LETTER_WORDS).lower()
    gw = WordleGWindow()
    wordle(ActualWord, gw)


# def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
# def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
# def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
# CORRECT_COLOR = "#66BB66"       # Light green for correct letters
# PRESENT_COLOR = "#CCBB66"       # Brownish yellow for misplaced letters
# MISSING_COLOR = "#999999"       # Gray for letters that don't appear
# UNKNOWN_COLOR = "#FFFFFF"       # Undetermined letters are white
# KEY_COLOR = "#DDDDDD"           # Keys are colored light gray






