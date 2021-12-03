

file = open('03.txt', 'r')
lines = file.readlines()
binums = sorted([l.strip() for l in lines])

def get_occurences(i, lst):
    zeroes = list(filter(lambda x: x[i] == '0', lst))
    ones = lst[len(zeroes):]
    return (zeroes, ones)

def most_frequent(lst1, lst2):
    return lst1 if len(lst2) < len(lst1) else lst2

def least_frequent(lst1, lst2):
    return lst2 if len(lst1) > len(lst2) else lst1


# PART 1
counter = [0 for _ in range(len(binums[0]))]
for i in range(len(binums)):
    for j in range(len(binums[i])):
        counter[j] += (2 * int(binums[i][j])) - 1

gamma = ''.join(['0' if num < 1 else '1' for num in counter])
epsilon = ''.join(['0' if gamma[i] == '1' else '1' for i in range(len(gamma))])
print('DAY 3 | PART 1:', int(gamma, 2) * int(epsilon, 2))


# PART 2
zeroes, ones = get_occurences(0, binums)
oxygen = most_frequent(zeroes, ones)
co2 = least_frequent(zeroes, ones)

for i in range(1, len(counter)):
    if len(oxygen) > 1:
        _zeroes, _ones = get_occurences(i, oxygen)
        oxygen = most_frequent(_zeroes, _ones)

    if len(co2) > 1:
        _zeroes, _ones = get_occurences(i, co2)
        co2 = least_frequent(_zeroes, _ones)
print('DAY 3 | PART 2:', int(oxygen[0], 2) * int(co2[0], 2))
