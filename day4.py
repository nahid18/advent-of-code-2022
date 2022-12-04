INPUT_FILE="data/day4.txt"

with open(INPUT_FILE) as fh:
    total = 0
    lines = fh.read().splitlines()
    for line in lines:
        a, b = line.split(",")
        low_a, high_a = a.split("-")
        low_b, high_b = b.split("-")
        low_a, high_a, low_b, high_b = int(low_a), int(high_a), int(low_b), int(high_b)
        
        if low_a == low_b or high_a == high_b:
            total += 1
        elif low_a < low_b and high_a > high_b:
            total += 1
        elif low_a > low_b and high_a < high_b:
            total += 1
            
    print("ROUND 1:", total)
        