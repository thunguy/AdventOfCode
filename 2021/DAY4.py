class Board():
    def __init__(self, board):
        self.board = board
        self.rows = [set(row) for row in board]
        self.columns = [set(row) for row in zip(*board)]

    def check_num(self, num):
        for row in self.rows:
            if num in row: row.remove(num)
        for col in self.columns:
            if num in col: col.remove(num)
        return self.check_row(num) or self.check_column(num)

    def check_row(self, num):
        if any(len(row) == 0 for row in self.rows):
            return sum(list(map(sum, self.rows))) * num

    def check_column(self, num):
        if any(len(col) == 0 for col in self.columns):
            return sum(list(map(sum, self.columns))) * num


file = open('04.txt', 'r')
text = file.read()
lines = text.split('\n\n')
draws, *matrices = lines
matrices = [[list(map(int, row.split())) for row in matrix.split('\n')] for matrix in matrices]

draws = list(map(int, draws.split(',')))
boards = [Board(board=matrix) for matrix in matrices]

# PART 1
def play_bingo_part_1():
    for draw in draws:
        for board in boards:
            score = board.check_num(draw)
            if score:
                return score

# PART 2
def play_bingo_part_2():
    bingos, num_boards = set(), len(boards)
    for draw in draws:
        for i, board in enumerate(boards):
            if i not in bingos:
                score = board.check_num(draw)
                if score:
                    bingos.add(i)
                if len(bingos) == num_boards:
                    return score

print('DAY 4 | PART 1:', play_bingo_part_1())
print('DAY 4 | PART 2:', play_bingo_part_2())