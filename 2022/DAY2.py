A, B, C, X, Y, Z = 'A', 'B', 'C', 'X', 'Y', 'Z'

with open('inputs/02.txt') as file:
    points = {X: 1, Y: 2, Z: 3}
    mapper = {A: X, B: Y, C: Z}
    rounds = [(mapper[a], b) for a, b in [line.split() for line in file]]
    shapes = {X: (Y, Z), Y: (Z, X), Z: (X, Y)}  # SHAPE1: (SUPERIOR SHAPE2, INFERIOR SHAPE3)

def get_round_score(opponent, mine):
    score = points[mine]
    score += 3 if mine == opponent else \
             6 if mine == shapes[opponent][0] else 0
    return score

outcomes = {
    X: {k: v[1] for k, v in shapes.items()},  # X = LOSE
    Y: {k: k for k, _ in shapes.items()},     # Y = TIE
    Z: {k: v[0] for k, v in shapes.items()}   # Z = WIN
}

print(f'DAY 2 | PART 1: {sum([get_round_score(opponent, mine) for opponent, mine in rounds])}')
print(f'DAY 2 | PART 2: {sum([get_round_score(shape, outcomes[event][shape]) for shape, event in rounds])}')
