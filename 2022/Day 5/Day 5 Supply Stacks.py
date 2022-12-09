# ===============================
# AUTHOR        : Johan van der Merwe
# CREATE DATE   : 07 Dec 2022
# PURPOSE       : For Advent of code
# SPECIAL NOTES : Contains final code for part 1 of day 5
# ===============================
# Change History:
# - 
# ==================================

import os
import sys
from dotenv import load_dotenv

load_dotenv()
HOME_DIR = os.getenv("HOME_DIR")
sys.path.append(f'{HOME_DIR}AdventOfCode')

from _modules.advent_helpers import strip_linebreak as slb

def build_stacks(inlist:list):
    index_map = {}
    outlist = []

    # Get the length of the stack from the file
    len_stack = int(inlist[-1][-2])

    # Go thorugh each stack column
    for i in range(0,len_stack):
        in_ = {}

        # Get the index of the stack columns values
        for n in inlist[-1]:
            if n.isnumeric and n == str(i + 1):
                in_[i] = inlist[-1].index(n)
        index_map[i] = in_[i]

        _ = []
        # Go trought the stack in reverse to gather all values
        for item in reversed(inlist):
            if item[index_map[i]].isalpha():
                _.append(item[index_map[i]])
        outlist.append(_)
    
    return outlist


with (open(f"{HOME_DIR}AdventOfCode\\2022\\Day 5\\Puzzle input.txt") as f):
    stacks = []
    for line in f.readlines()[:9]:
        stacks.append(slb(line))

    print(build_stacks(stacks))
    
