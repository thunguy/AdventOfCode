file = open('03.txt', 'r')
lines = file.readlines()
binums = [l.strip() for l in lines]

counter = [0 for _ in range(len(binums[0]))]

for i in range(len(binums)):
    for j in range(len(binums[i])):
        counter[j] += (2 * int(binums[i][j])) - 1

gamma = ''.join(['0' if num < 1 else '1' for num in counter])
epsilon = ''.join(['0' if gamma[i] == '1' else '1' for i in range(len(gamma))])

# oxygen =
# co2 =

print('DAY 3 | PART 1:', int(gamma, 2) * int(epsilon, 2))

