def build_stacks(crates: list) -> list:
    crates = [[c.replace('[', '').replace(']', '')
               for c in c.replace('    ', ' ').split(' ')]
              for c in crates.splitlines()][:-1]
    stacks = []
    for stack in zip(*crates):
        stack = [c for c in stack if c]
        stack.reverse()
        stacks += [stack]
    return stacks

def build_manual(orders: list) -> list:
    manual = [(int(n) for n in o.split()[1::2])
              for o in orders.splitlines()]
    manual.reverse()
    return manual

def cratemover(orders, crates, type):
    manual = build_manual(orders)
    stacks = build_stacks(crates)

    while manual:
        n, a, b = manual.pop()
        craned = stacks[a-1][-n:][::-1]
        if type == 9001:
            craned = stacks[a-1][-n:]
        stacks[b-1].extend(craned)
        stacks[a-1] = stacks[a-1][:-n]
    return ''.join([s[-1] for s in stacks])

with open('inputs/05.txt') as f:
    crates, orders = f.read().split('\n\n')

print(f'DAY 5 | PART 1: {cratemover(orders, crates, 9000)}')
print(f'DAY 5 | PART 2: {cratemover(orders, crates, 9001)}')
