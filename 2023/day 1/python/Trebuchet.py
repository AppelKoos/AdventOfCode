import re    

# part 1
with open("./2023/day 1/puzzle_input.txt") as f:  
    calibration_val = 0
    for val in f.readlines():
        if any(char.isdigit() for char in val):
            numberL = re.search(r'\d', val).group()
            numberR = re.search(r'\d', val[::-1]).group()
            # print(int(numberL), '++', int(numberR) , '=', numberL + numberR)
            calibration_val += int(numberL + numberR)
    print("day 1: solution:", calibration_val)

# part 2

def insert_num(line: str):
    # The scrope of the challenge is narrow and the words can be hardcoded
    # num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    line = line.replace("zero", "z0ero")
    line = line.replace("one", "o1ne")
    line = line.replace("two", "t2wo")
    line = line.replace("three", "t3hree")
    line = line.replace("four", "f4our")
    line = line.replace("five", "f5ive")
    line = line.replace("six", "s6ix")
    line = line.replace("seven", "s7even")
    line = line.replace("eight", "e8ight")
    line = line.replace("nine", "n9ine")
    return line

with open("./2023/day 1/puzzle_input.txt") as f:  
    calibration_val = 0
    for val in f.readlines():
        val = insert_num(val)
        numberL = re.search(r'\d', val).group()
        numberR = re.search(r'\d', val[::-1]).group()
        # print(int(numberL), '++', int(numberR) , '=', numberL + numberR)
        calibration_val += int(numberL + numberR)
    print("day 2: solution:",calibration_val)
