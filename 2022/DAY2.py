A, X = 'A', 'X'  # rock
B, Y = 'B', 'Y'  # paper
C, Z = 'C', 'Z'  # scissor

with open("inputs/02.txt") as file:
    shapes = {A: X, B: Y, C: Z}
    rounds = [(shapes[a], b) for a, b in [line.split() for line in file]]
    events = {X: (1, Y, Z), Y: (2, Z, X), Z: (3, X, Y)}

score = 0
for round in rounds:
    opponent, mine = round
    score += events[mine][0]
    if mine == events[opponent][1]:
        score += 6
    if mine == opponent:
        score += 3
print(f'PART 1: {score}')

score = 0
for round in rounds:
    shape, result = round
    if result == Z:
        score += events[events[shape][1]][0]
        score += 6
    elif result == Y:
        score += events[shape][0]
        score += 3
    else:
        score += events[events[shape][2]][0]
print(f'PART 2: {score}')





