INPUT_FILE="data/day2.txt"

# Rock = A , Paper = B, Scissors = C

def get_winner(opponent, me):
    if me == opponent:
        return "DRAW"
    if me == "A" and opponent == "C":
        return "WIN"
    if me == "B" and opponent == "A":
        return "WIN"
    if me == "C" and opponent == "B":
        return "WIN"
    if me == "C" and opponent == "A":
        return "LOSE"
    if me == "A" and opponent == "B":
        return "LOSE"
    if me == "B" and opponent == "C":
        return "LOSE"


item_dict = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

item_score = {
    "A": 1,
    "B": 2,
    "C": 3
}

result_score = {
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0
}

# ROUND 1
with open(INPUT_FILE) as f:
    total_score = 0
    rounds = f.read().splitlines()
    for r in rounds:
        opponent , me = r.split()
        result = get_winner(opponent, item_dict[me])
        my_score = item_score[item_dict[me]] + result_score[result]
        total_score += my_score
    print("ROUND 1:", total_score)


# ROUND 2
def get_correct_option(strategy, opponent):
    if strategy == "DRAW":
        return opponent
    if strategy == "WIN":
        return "A" if opponent == "C" else "B" if opponent == "A" else "C"
    if strategy == "LOSE":
        return "C" if opponent == "A" else "A" if opponent == "B" else "B"

strategy_dict = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN"
}

with open(INPUT_FILE) as f:
    new_score = 0
    rounds = f.read().splitlines()
    for r in rounds:
        opponent, strategy = r.split()
        my_option = get_correct_option(strategy_dict[strategy], opponent)
        my_score = item_score[my_option] + result_score[strategy_dict[strategy]]
        new_score += my_score
    print("ROUND 2:", new_score)