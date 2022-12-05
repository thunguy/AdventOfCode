with open('inputs/04.txt') as f:
    ranges = [[n.split('-') for n in l.split(',')] for l in f.read().splitlines()]
    ranges = [sorted([(int(r1), int(r2)) for r1, r2 in range]) for range in ranges]

# range completely overlaps
PART1 = sum(1 for r1, r2 in ranges
            if (r1[1] >= r2[1]) or
               (r1[1] <= r2[1] and r1[0] == r2[0]))

# range partially overlaps
PART2 = sum(1 for r1, r2 in ranges if r1[1] >= r2[0])

print(f'DAY 4 | PART 1: {PART1}')
print(f'DAY 4 | PART 2: {PART2}')
