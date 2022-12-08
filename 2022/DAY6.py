with open('inputs/06.txt') as f:
    data = f.read().strip()

def distance_to_marker(data: str, n: int) -> int:
    A, B = 0, 0

    while B - A < n:
        if data[B] in set(data[A:B]):
            A = data.index(data[B], A) + 1
        B += 1
    return B

print(f'DAY 6 | PART 1: {distance_to_marker(data, 4)}')
print(f'DAY 6 | PART 2: {distance_to_marker(data, 14)}')
