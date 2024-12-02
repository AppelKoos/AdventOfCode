# Pair up the smallest numbers and calculate the difference between them

print("Part 1")
with(open(f"..\\puzzle_input.txt") as f):
    left_list = []
    right_list = []

    for distance_pair in f.readlines():
        l_item = int(distance_pair[0:distance_pair.find(' ')].strip())
        r_item = int(distance_pair[distance_pair.rfind(' ')+1:].strip())
        left_list.append(l_item)
        right_list.append(r_item)
        # print(f"{l_item} {r_item}")

    left_list.sort()
    right_list.sort()
    sum_delta = 0
    for i in range(0, len(left_list)):
        sum_delta += abs(left_list[i]-right_list[i])
        # print(f"{abs(left_list[i]-right_list[i])}")
    print(sum_delta)

print("Part 2")
with(open(f"..\\puzzle_input.txt") as f):
    left_list = []
    right_list = []

    for distance_pair in f.readlines():
        l_item = int(distance_pair[0:distance_pair.find(' ')].strip())
        r_item = int(distance_pair[distance_pair.rfind(' ')+1:].strip())
        left_list.append(l_item)
        right_list.append(r_item)
        # print(f"{l_item} {r_item}")

    similarity_score = 0
    for num in left_list:
        same_count = 0
        for rnum in right_list:
            if rnum == num:
                same_count += 1
        similarity_score += num * same_count

    print(similarity_score)
