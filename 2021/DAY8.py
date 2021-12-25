#  aaaa                aaaa      aaaa
# b    c         c         c         c    b    c
# b    c         c         c         c    b    c
#                      dddd      dddd      dddd
# e    f         f    e              f         f
# e    f         f    e              f         f
#  gggg                gggg      gggg


#  aaaa      aaaa      aaaa      aaaa      aaaa
# b         b              c    b    c    b    c
# b         b              c    b    c    b    c
#  dddd      dddd                dddd      dddd
#      f    e    f         f    e    f         f
#      f    e    f         f    e    f         f
#  gggg      gggg                gggg      gggg

file = open('08.txt', 'r')
lines = file.readlines()
displays = [l.split('|') for l in lines]

sequences = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
segment_map = {frozenset(set(s)): str(i) for i, s in enumerate(sequences)}

def part_1(displays):
    displays = [get_digits(*d) for d in displays]
    all_digits = sum(displays, [])
    return sum([1 for d in all_digits if d in set('1478')])

def part_2(displays):
    displays = [get_digits(*d) for d in displays]
    nums = [int(''.join(x))for x in displays]
    return sum(nums)

def get_digits(digits, tests):
    digits = [set(x) for x in digits.split()]
    tests = [set(x) for x in tests.split()]

    one = [d for d in digits if len(d) == 2][0] # -> {c, f}
    seven = [d for d in digits if len(d) == 3][0] # -> {a, c, f}
    four = [d for d in digits if len(d) == 4][0] # -> {b, c, d, f}
    eight = [d for d in digits if len(d) == 7][0] # -> {a, b, c, d, e, f, g}

    fivers = [d for d in digits if len(d) == 5]
    sixers = [d for d in digits if len(d) == 6]

    adg = set.intersection(*fivers)
    abfg = set.intersection(*sixers)
    a = seven - one
    bd = four - one
    eg = eight - four - a
    g = adg & eg
    e = eg - g
    d = bd & adg
    b = bd - d
    f = abfg - a - b - g
    c = one - f

    keys = [a, b, c, d, e, f, g]
    vals = list('abcdefg')

    decoder = {list(k)[0]: v for k, v in zip(keys, vals)}
    decoded = [frozenset(decoder[x] for x in test) for test in tests]
    return [segment_map[d] for d in decoded]

print(f'DAY 8 | PART 1: {part_1(displays)}')
print(f'DAY 8 | PART 2: {part_2(displays)}')