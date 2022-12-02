with open('05.txt') as file:
    lines = [line.strip().split(' -> ') for line in file.readlines()]
    data = [[xy1.split(','), xy2.split(',')] for xy1, xy2 in lines]
    coordinates = [[(int(x1), int(y1)), (int(x2), int(y2))] for (x1, y1), (x2, y2) in data]
    vertizontals = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], coordinates))

class Diagram():
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.Xmax = sorted([x1 for (x1, _), _ in coordinates] + [x2 for _, (x2, _) in coordinates])[-1]
        self.Ymax = sorted([y1 for (_, y1), _ in coordinates] + [y2 for _, (_, y2) in coordinates])[-1]
        self.grid = [[0 for _ in range(self.Xmax + 1)] for _ in range(self.Ymax + 1)]

    def linefill(self, endpoints):
        (x1, y1), (x2, y2) = sorted(endpoints)
        if x1 == x2:
            for y in range(y1, y2+1):
                self.grid[y][x1] += 1
        elif y1 == y2:
            for x in range(x1, x2+1):
                self.grid[y1][x] += 1
        else:
            Xs = range(x1, x2+1)
            Ys = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
            for x, y in zip(Xs, Ys):
                self.grid[y][x] += 1

    def mapper(self):
        for coords in self.coordinates:
            self.linefill(coords)

    def overlaps(self):
        self.mapper()
        return len([num for row in self.grid for num in row if num > 1])

diagram_part_1 = Diagram(vertizontals)
diagram_part_2 = Diagram(coordinates)

print(f'DAY 5 | PART 1: {diagram_part_1.overlaps()}')
print(f'DAY 5 | PART 2: {diagram_part_2.overlaps()}')