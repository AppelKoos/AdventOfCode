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
import re
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


def perform_procedure(stack_list:list, action_list:list):
    for procedure in action_list:
        action_list = re.findall(r'\d+', procedure)

        movee = int(action_list[0])
        froml = int(action_list[1]) - 1
        tol = int(action_list[2]) - 1
        print(movee)
        print(f'--from {stack_list[froml]}')
        print(f'--to {stack_list[tol]}')

        if len(stack_list[froml]) < movee:
            print('----------------from list to short----------------')
            print(f'tried the following: {action_list} from {stack_list[froml]} to {stack_list[tol]}')
        else:
            # Incorrect guess 1 DLFGJDJZW
            # Incorrect guess 1 DLFGQWTZW
            if movee == 1:
                for e in reversed(stack_list[froml]):
                    print(movee)
                    print(f'%%from {stack_list[froml]}')
                    print(f'%%to {stack_list[tol]}')
                    if movee <= 0:
                        print(f'%%from {stack_list[froml]}')
                        print(f'%%to {stack_list[tol]}')
                        break
                    stack_list[tol].append(e)
                    stack_list[froml].pop()
                    movee -= 1
            else:
                _ = []
                for e in reversed(stack_list[froml]):
                    print(movee)
                    print(f'%%from {stack_list[froml]}')
                    print(f'%%to {stack_list[tol]}')
                    if movee <= 0:
                        for i in reversed(_):
                            stack_list[tol].append(i)
                        print(f'%%from {stack_list[froml]}')
                        print(f'%%to {stack_list[tol]}')
                        break
                    _.append(e)
                    stack_list[froml].pop()
                    movee -= 1
    return stack_list


def print_result(inlist:list):
    _ = ''
    for crate in inlist:
        _ += f'{crate[-1]}'
    print(f'The top crates in each stack is: {_}')


# Read in the stacks
stacks = []
with (open(f"{HOME_DIR}AdventOfCode\\2022\\Day 5\\Puzzle input.txt") as f):
    for line in f.readlines()[:9]:
        stacks.append(slb(line))

    stacks = build_stacks(stacks)

# Read in the procedures
stack_procedures = []
with (open(f"{HOME_DIR}AdventOfCode\\2022\\Day 5\\Puzzle input.txt") as f):
    for line in f.readlines()[10:]:
        stack_procedures.append(slb(line))

# Perform procedure
stacks = perform_procedure(stacks, stack_procedures)

# Print result
print_result(stacks)
