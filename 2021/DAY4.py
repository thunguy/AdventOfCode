import numpy as np


class Board():
    def __init__(self, board):
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
        for row in self.rows:
            if len(row) == 0:
                return sum(list(map(sum, self.rows))) * num


    def check_column(self, num):
        for col in self.columns:
            if len(col) == 0:
                return sum(list(map(sum, self.columns))) * num


file = open('04.txt', 'r')
text = file.read()
lines = text.split('\n\n')
draws, *matrices = lines

draws = list(map(int, draws.split(',')))
matrices = [np.array([list(map(int, row.split())) for row in matrix.split('\n')]) for matrix in matrices]

boards = [Board(board=matrix) for matrix in matrices]

# PART 1
def play_bingo_part_1():
    for draw in draws:
        for board in boards:
            bingo = board.check_num(num=draw)
            if bingo:
                return bingo

print('DAY 4 | PART 1:', play_bingo_part_1())
