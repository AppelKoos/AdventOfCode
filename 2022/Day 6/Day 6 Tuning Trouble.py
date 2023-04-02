# ===============================
# AUTHOR        : Johan van der Merwe
# CREATE DATE   : 18 Dec 2022
# PURPOSE       : For Advent of code
# SPECIAL NOTES : Contains final code for part 1 & 2 of day 6
# ===============================
# Change History:
# - 
# ==================================

import os
import sys
from dotenv import load_dotenv

load_dotenv()
HOME_DIR = os.getenv("HOME_DIR")

with (open(f"{HOME_DIR}AdventOfCode\\2022\\Day 6\\Puzzle input.txt") as f):
    # Part 1
    chars = []
    i = 0

    for c in f.readline():
        if len(chars) >= 4:
            # Compare the 4 characters
            if (len(chars) == len(set(chars))):
                print(f'Start of packet marker detected at position: {i}')
                break
            # Clear out first added char
            chars.pop(0)

        # Add in new char
        chars.append(c)
        i += 1

with (open(f"{HOME_DIR}AdventOfCode\\2022\\Day 6\\Puzzle input.txt") as f):
    # Part 2
    chars = []
    i = 0
    for c in f.readline():
        if len(chars) >= 14:
            # Compare the 4 characters
            if (len(chars) == len(set(chars))):
                print(f'Start of message marker detected at position: {i}')
                break
            # Clear out first added char
            chars.pop(0)

        # Add in new char
        chars.append(c)
        i += 1
