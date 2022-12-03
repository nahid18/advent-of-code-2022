INPUT_FILE="data/day1.txt"

elf_dict = {}
current_elf = 1
with open(INPUT_FILE, "r") as f:
    current_elf_sum = 0
    for line in f:
        if line.strip() != '':
            current_elf_sum += int(line.strip())
        else:
            elf_dict[current_elf] = current_elf_sum
            current_elf += 1
            current_elf_sum = 0


max_value = max(elf_dict.values())
print("ROUND 1:", max_value)

top_3 = sorted(elf_dict.items(), key=lambda x: x[1], reverse=True)[:3]
top_3_value_sum = sum([x[1] for x in top_3])
print("ROUND 2:", top_3_value_sum)