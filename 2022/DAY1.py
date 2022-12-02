with open('inputs/01.txt') as f:
    calories = [sum([int(c) for c in l.strip().split('\n')]) for l in f.read().split('\n\n')]

print(f'DAY 1 | PART 1: {max(calories)}')
print(f'DAY 1 | PART 2: {sum(sorted(calories)[-3:])}')
