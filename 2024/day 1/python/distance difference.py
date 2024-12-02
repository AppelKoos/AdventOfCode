# Pair up the smallest numbers and calculate the difference between them

with(open(f"..\\puzzle_input.txt") as f):
    # print(f.readlines())
    left_list = []
    right_list = []

    for distance_pair in f.readlines():
        l_item = int(distance_pair[0:distance_pair.find(' ')].strip())
        r_item = int(distance_pair[distance_pair.rfind(' ')+1:].strip())
        left_list.append(l_item)
        right_list.append(r_item)
        print(f"{l_item} {r_item}")

    print(left_list)
    left_list.sort()
    print(left_list)
    print(right_list)
    right_list.sort()
    print(right_list)

    sum_delta = 0
    for i in range(0, len(left_list)):
        sum_delta += abs(left_list[i]-right_list[i])
        print(f"{abs(left_list[i]-right_list[i])}")
    print(sum_delta)