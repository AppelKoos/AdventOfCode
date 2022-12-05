# ===============================
# AUTHOR        : Johan van der Merwe
# CREATE DATE   : 04 Dec 2022
# PURPOSE       : For Advent of code
# SPECIAL NOTES : Contains final code for part 2 of day 4
# ===============================
# Change History:
# - 
# ==================================

import os
from dotenv import load_dotenv

load_dotenv()
HOME_DIR = os.getenv("HOME_DIR")

def strip_linebreak(l:str):
    if l[-1] == '\n':
        l = l[:-1]
    return l


with (open(f"{HOME_DIR}AdventOfCode\\2022\\Day 4\\Puzzle input.txt") as f):
    overlapping_pairs = 0

    for line in f.readlines():
        pair = strip_linebreak(line).split(',')

        min_p1 = int(pair[0].split('-')[0])
        max_p1 = int(pair[0].split('-')[1])
        min_p2 = int(pair[1].split('-')[0])
        max_p2 = int(pair[1].split('-')[1])
        
        rng1 = list(range(min_p1, max_p1 + 1))
        rng2 = list(range(min_p2, max_p2 + 1))

        if min(rng2) in rng1 or max(rng2) in rng1:
                overlapping_pairs += 1
        elif min(rng1) in rng2 or max(rng1) in rng2:
                overlapping_pairs += 1

print(overlapping_pairs)
