with open("inputs/02.txt") as file:
    points = {'X': 1, 'Y': 2, 'Z': 3}
    shapes = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    rounds = [(shapes[a], b) for a, b in [line.split() for line in file]]
    events = {'X': {'superior': 'Y', 'inferior': 'Z'},
              'Y': {'superior': 'Z', 'inferior': 'X'},
              'Z': {'superior': 'X', 'inferior': 'Y'}}

score = 0
for opponent, mine in rounds:
    score += points[mine]
    score += 3 if mine == opponent else \
             6 if mine == events[opponent]['superior'] else \
             0
print(f'DAY 2 | PART 1: {score}')

score = 0
lose, draw, win = 'X', 'Y', 'Z'
for opponent, outcome in rounds:
    score += 3 + points[opponent] if outcome == draw else \
             6 + points[events[opponent]['superior']] if outcome == win else \
             0 + points[events[opponent]['inferior']]
print(f'DAY 2 | PART 2: {score}')
