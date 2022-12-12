from math import prod


FILE = open('inputs/11.txt').read().strip().splitlines()
NOTES, MONKEYS, DIVISOR = None, None, None


def parse_notes(file=FILE) -> list:
    global NOTES, DIVISOR, MONKEYS
    NOTES = [[
        [int(n) for n in a.split(', ')],
        b.split('= ')[1],
        int(c.split('by ')[-1]),
        int(d.split()[-1]),
        int(e.split()[-1]),
    ] for a, b, c, d, e in [
        [l.split(': ')[1] for l in file[n:n+7][1:] if l]
        for n in range(0, len(file), 7)
    ]]
    DIVISOR = prod([n[2] for n in NOTES])
    MONKEYS = len(NOTES)
    return NOTES


def monkey_business(rounds: int, scared: bool) -> int:
    notes, levels = parse_notes(), [0] * MONKEYS
    for _ in range(rounds):
        for M, (I, O, D, T, F) in enumerate(notes):
            for _ in range(len(I)):
                old = I.pop(0)
                new = eval(O) % DIVISOR if scared else eval(O) // 3
                items = notes[T][0] if new % D == 0 else notes[F][0]
                items += [new]
                levels[M] += 1
    levels.sort()
    return prod(levels[-2:])


print(f'DAY 11 | PART 1: {monkey_business(20, False)}')
print(f'DAY 11 | PART 2: {monkey_business(10000, True)}')
