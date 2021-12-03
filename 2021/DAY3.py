file = open('03.txt', 'r')
lines = file.readlines()
binums = [l.strip() for l in lines]


def get_occurences(i, lst):
    zeroes = list(filter(lambda x: x[i] == '0', lst))
    ones = list(filter(lambda x: x[i] == '1', lst))
    return (zeroes, ones)


# PART 1
counter = [0 for _ in range(len(binums[0]))]
for i in range(len(binums)):
    for j in range(len(binums[i])):
        counter[j] += (2 * int(binums[i][j])) - 1

gamma = ''.join(['0' if num < 1 else '1' for num in counter])
epsilon = ''.join(['0' if gamma[i] == '1' else '1' for i in range(len(gamma))])
print('DAY 3 | PART 1:', int(gamma, 2) * int(epsilon, 2))


# PART 2
init_zeroes = list(filter(lambda x: x[0] == '0', binums))
init_ones = list(filter(lambda x: x[0] == '1', binums))

oxygen = init_zeroes if len(init_ones) < len(init_zeroes) else init_ones
co2 = init_ones if len(init_zeroes) > len(init_ones) else init_zeroes

for i in range(1, len(counter)):
    if len(oxygen) > 1:
        zeroes, ones = get_occurences(i, oxygen)
        oxygen = zeroes if len(ones) < len(zeroes) else ones

    if len(co2) > 1:
        zeroes, ones = get_occurences(i, co2)
        co2 = ones if len(zeroes) > len(ones) else zeroes
print('DAY 3 | PART 2:', int(oxygen[0], 2) * int(co2[0], 2))
