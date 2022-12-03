ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('inputs/03.txt') as file:
    sacks = [l for l in file.read().strip().split('\n')]
    order = {char: i for i, char in enumerate(ALPHA, 1)}

PART1 = sum(order[i]
            for s in sacks
            for i in set(s[:len(s)//2]) & set(s[len(s)//2:]))

PART2 = sum(order[i]
            for s1, s2, s3 in zip(*(iter(sacks),) * 3)
            for i in set(s1) & set(s2) & set(s3))

print(f'DAY 3 | PART 1: {PART1}')
print(f'DAY 3 | PART 2: {PART2}')
