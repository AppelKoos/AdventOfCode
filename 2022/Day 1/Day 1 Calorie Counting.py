# ===============================
# AUTHOR        : Johan van der Merwe
# CREATE DATE   : 01 Dec 2022
# PURPOSE       : For Advent of code
# SPECIAL NOTES : Contains final code for part 1 & 2 of day 1
# ===============================
# Change History:
# - Fixed notes (03 Dec 2022)
# ==================================

import os
from dotenv import load_dotenv

load_dotenv()
HOME_DIR = os.getenv("HOME_DIR")
elf_total_calories = []

with(open(f"{HOME_DIR}AdventOfCode\\2022\\Day 1\\puzzle input.txt") as f):
    elf_total = 0
    # Read in elf calorie values
    for l in f.readlines():
        if l == "\n":
            # Skip and reset if value is \n
            elf_total_calories.append(elf_total)
            elf_total = 0
        else:
            elf_total += int(l[:-1])

# Take the top 3 calorie counts and sum them
elf_total_calories.sort(reverse=True)
max_calories = elf_total_calories[:3]
sum_calories = sum(max_calories)

print('The top 3 elves have the following calorie counts:')
for i in max_calories: print(f'-\t-\t{i}')
print(f'The sum of the top 3 calorie hoaders is: \n-\t-\t{sum_calories}')
