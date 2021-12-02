file = open('02.txt', 'r')
lines = file.readlines()
directions = [l.split() for l in lines]
directions = list(map(lambda x: [x[0], int(x[1])], directions))

x1, y1, y2 = 0, 0, 0
for direction, displacement in directions:
    if direction == 'forward':
        x1 += displacement
        y2 += (y1 * displacement)
    elif direction == 'up':
        y1 -= displacement
    elif direction == 'down':
        y1 += displacement
print('DAY 2 | PART 1:', x1 * y1)
print('DAY 2 | PART 2:', x1 * y2)