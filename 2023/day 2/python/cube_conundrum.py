def find_colour_max(game:str, colour:str, max=0):
    c_index = game.lower().find(colour)
    
    try: 
        curr_num = int(game[c_index-3:c_index])

        # print('DEBUG: curr_num:', curr_num, 'max:', max)
        if curr_num > max:
            max = curr_num

        # There might be more
        next_num = find_colour_max(game[c_index + len(colour):], colour, max)
        if next_num > max:
            max = next_num

    except ValueError:
        pass

    return max


# Day 1
with open("./2023/day 2/puzzle_input.txt") as f:
    cubes_max = {
        'game'  : 0,
        'red'   : 12,
        'green' : 13,
        'blue'  : 14
    }

    for gameplay in f.readlines():

        red_max = find_colour_max(gameplay, 'red')
        green_max = find_colour_max(gameplay, 'green')
        blue_max = find_colour_max(gameplay, 'blue')
        
        if  red_max <= cubes_max['red'] and green_max <= cubes_max['green'] and blue_max <= cubes_max['blue']:
            cubes_max['game'] += int(gameplay[gameplay.find('Game ')+len('Game '):gameplay.find(':')])  # Game Id
            # print(f'INFO:::: red: {red_max} <= {cubes_max["red"]} | green: {green_max} <= {cubes_max["green"]} | blue: {blue_max} <= {cubes_max["blue"]}')
            # print(gameplay.strip())
        # else:
            # print('####NOT VALID', gameplay[:gameplay.find(':')], 'NOT VALID####')
            # print(f'INFO:::: red: {red_max} > {cubes_max["red"]} | green: {green_max} > {cubes_max["green"]} | blue: {blue_max} > {cubes_max["blue"]}')
            # print(gameplay.strip())        
        
        # print(f'-----------------{cubes_max["game"]}-------------------')

    print('Day 1 Answer:', cubes_max['game'])


# Day 2
with open("./2023/day 2/puzzle_input.txt") as f:
    game_calc = 0

    for gameplay in f.readlines():
        cubes_min = {
            'red'   : 0,
            'green' : 0,
            'blue'  : 0
        }

        red_min = find_colour_max(gameplay, 'red')
        green_min = find_colour_max(gameplay, 'green')
        blue_min = find_colour_max(gameplay, 'blue')

        # print(f'INFO:::: red: {red_min} | green: {green_min} | blue: {blue_min}')

        if red_min > cubes_min['red'] or green_min > cubes_min['green'] or blue_min > cubes_min['blue']:
            cubes_min['red'] = red_min
            cubes_min['green'] = green_min
            cubes_min['blue'] = blue_min

        # print(f"INFO:::: red: {cubes_min['red']} | green: {cubes_min['green']} | blue: {cubes_min['blue']}")
        game_calc += cubes_min['red'] * cubes_min['green'] * cubes_min['blue']
        
        # print(f'-----------------{game_calc}-------------------')

    print('Day 2 Answer:', game_calc)
