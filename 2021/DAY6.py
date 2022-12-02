from collections import Counter

file = open('06.txt', 'r')
init_states = [int(s) for s in file.readlines()[0].split(',')]

def num_fish(days):
    fish = Counter(init_states)

    for i in range(days):
        fish[(i+7) % 9] += fish[i % 9]
    return sum(fish.values())

print(f'DAY 6 | PART 1: {num_fish(80)}')
print(f'DAY 6 | PART 2: {num_fish(256)}')
