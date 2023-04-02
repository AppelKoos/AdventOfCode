# ===============================
# AUTHOR        : Johan van der Merwe
# CREATE DATE   : 04 Dec 2022
# PURPOSE       : Commonly used functions for Advent of Code
# ===============================
# Change History:
# - 
# ==================================

def strip_linebreak(l:str):
    if l[-1] == '\n':
        l = l[:-1]
    return l