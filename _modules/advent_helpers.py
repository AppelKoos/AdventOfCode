def strip_linebreak(l:str):
    if l[-1] == '\n':
        l = l[:-1]
    return l