with open("inputs/02.txt") as file:
    points = {'X': 1, 'Y': 2, 'Z': 3}
    mapper = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    rounds = [(mapper[a], b) for a, b in [line.split() for line in file]]
    shapes = {'X': {'superior': 'Y', 'inferior': 'Z'},
              'Y': {'superior': 'Z', 'inferior': 'X'},
              'Z': {'superior': 'X', 'inferior': 'Y'}}

def get_round_score(opponent, mine):
    score = points[mine]
    score += 3 if mine == opponent else \
             6 if mine == shapes[opponent]['superior'] else \
             0
    return score

outcomes = {'X': {k:v['inferior'] for k,v in shapes.items()},
            'Y': {k:k for k,_ in shapes.items()},
            'Z': {k:v['superior'] for k,v in shapes.items()}}

print(f'DAY 2 | PART 1: {sum([get_round_score(opponent, mine) for opponent, mine in rounds])}')
print(f'DAY 2 | PART 2: {sum([get_round_score(opponent, outcomes[mine][opponent]) for opponent, mine in rounds])}')
