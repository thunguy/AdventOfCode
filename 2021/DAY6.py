from collections import Counter

file = open('06.txt', 'r')
fish = [int(s) for s in file.readlines()[0].split(',')]
init_counts = Counter(fish)

def num_fish(days):
    fish = [init_counts[i] for i in range(9)]
    for i in range(days):
        fish[(i+7) % 9] += fish[i % 9]
    return sum(fish)

print(f'DAY 6 | PART 1: {num_fish(80)}')
print(f'DAY 6 | PART 2: {num_fish(256)}')