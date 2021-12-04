import numpy as np

class Board():
    def __init__(self, board):
        board = np.array(board)
        self.board = board
        self.rows = [set(row) for row in board]
        self.columns = [set(col) for col in board.transpose()]

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
            bingo = board.check_num(num=draw)
            if bingo:
                return bingo

# PART 2
def play_bingo_part_2():
    wins = set()
    for draw in draws:
        for i in range(len(boards)):
            if i not in wins:
                bingo = boards[i].check_num(num=draw)

                if bingo:
                    wins.add(i)

                if len(wins) == len(boards):
                    return bingo

print('DAY 4 | PART 1:', play_bingo_part_1())
print('DAY 4 | PART 2:', play_bingo_part_2())