with open('05.txt') as file:
    lines = [line.strip().split(' -> ') for line in file.readlines()]
    data = [[xy1.split(','), xy2.split(',')] for xy1, xy2 in lines]
    coordinates = [[(int(x1), int(y1)), (int(x2), int(y2))] for (x1, y1), (x2, y2) in data]
    hv_lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], coordinates))


class Diagram():
    def __init__(self, coordinates):
        self.X = sorted([x1 for (x1, _), _ in coordinates] + [x2 for _, (x2, _) in coordinates])[-1]
        self.Y = sorted([y1 for (_, y1), _ in coordinates] + [y2 for _, (_, y2) in coordinates])[-1]
        self.grid = [[0 for _ in range(self.X + 1)] for _ in range(self.Y + 1)]

    def mark(self, location):
        (x1, y1), (x2, y2) = sorted(location)

        if x1 == x2:
            for i in range(y1, y2+1):
                self.grid[i][x1] += 1

        elif y1 == y2:
            for i in range(x1, x2+1):
                self.grid[y1][i] += 1

        else:
            runs = list(range(x1, x2+1))
            rises = list(range(y1, y2+1)) if y1 < y2 else list(reversed(range(y2, y1+1)))
            positions = [(runs[i], rises[i]) for i in range(len(runs))]
            for x, y in positions:
                self.grid[y][x] += 1

    def overlaps(self):
        return len(list(filter(lambda x: x > 1, [num for row in self.grid for num in row])))


diagram_part_1 = Diagram(hv_lines)
for line in hv_lines:
    diagram_part_1.mark(line)

diagram_part_2 = Diagram(coordinates)
for line in coordinates:
    diagram_part_2.mark(line)

print(f'DAY 5 | PART 1: {diagram_part_1.overlaps()}')
print(f'DAY 5 | PART 2: {diagram_part_2.overlaps()}')