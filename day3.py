INPUT_FILE="data/day3.txt"

import string

lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)

lower_case_dict = dict(zip(lower_case, range(1, 27)))
upper_case_dict = dict(zip(upper_case, range(27, 53)))

priority_dict = {**lower_case_dict, **upper_case_dict}


# ROUND 1
with open(INPUT_FILE) as f:
    total_score = 0
    rucksacks = f.read().splitlines()
    for r in rucksacks:
        middle = len(r) // 2
        first_part = r[:middle]
        second_part = r[middle:]
        mutual = set(first_part).intersection(set(second_part))
        total_score += sum([priority_dict[x] for x in mutual])
    print("ROUND 1:", total_score)

# ROUND 2
with open(INPUT_FILE) as fh:
    rucksacks = fh.read().splitlines()
    groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    common_items = []
    for group in groups:
        common_items.append(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))
    score = [sum([priority_dict[x] for x in item]) for item in common_items]
    print("ROUND 2:", sum(score))
    