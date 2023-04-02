# ===============================
# AUTHOR        : Johan van der Merwe
# CREATE DATE   : 02 Dec 2022
# PURPOSE       : For Advent of code
# SPECIAL NOTES : Contains final code for part 2 of day 2
# ===============================
# Change History:
# - Reformatted dicts (03 Dec 2022)
# ==================================

import os
from dotenv import load_dotenv
load_dotenv()
HOME_DIR = os.getenv('HOME_DIR')

def play_game(in1, in2):
    if in1=='Win':
        if in2 == 'Rock':
            return 2 + 6 # Score of paper
        elif in2 == 'Paper':
            return 3 + 6 # Score of scissors
        elif in2 == 'Scissors':
            return 1 + 6 # Score of rock
    
    if in1=='Draw':
        if in2 == 'Rock':
            return 1 + 3
        elif in2 == 'Paper':
            return 2 + 3
        elif in2 == 'Scissors':
            return 3 + 3

    if in1=='Lose':
        if in2 == 'Rock':
            return 3 # Score of scissors
        elif in2 == 'Paper':
            return 1 # Score of rock 
        elif in2 == 'Scissors':
            return 2 # Score of paper


def decode_game(es:str):
        INDEX1 = {
            'A': 'Rock',
            'B': 'Paper',
            'C': 'Scissors'
            }
        INDEX2 = {
            'X': 'Lose',
            'Y': 'Draw',
            'Z': 'Win'
            }
        return play_game(INDEX2[es[2]], INDEX1[es[0]])


with(open(f'{HOME_DIR}AdventOfCode\\2022\\Day 2\\puzzle input.txt') as f):
    total_score = 0
    for line in f.readlines():
        total_score += decode_game(line)

print(f'The simulated score is: {total_score}')
