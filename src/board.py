class Board:
    def __init__(self):
        self.grid = self.load_board()

    def load_board(self):
        file_path = "src/puzzles/dorm.txt"
        with open(file_path, 'r') as file:
            lines = file.readlines()

        board = []
        for line in lines:
            row = list(map(int, line.split()))
            board.append(row)

        return board

    def is_valid_move(self, row, column, value):
        # value cannot be equal to a value in the same row and column
        # value has to be unique to that subgrid
        pass

    def is_valid_board(self, board):
        # for the value in a cell, the entire row and entire column cannot contain the same value.
        for i in range(9):
            if len([n for n in i if n != 0]) != len(set(board[i])):
                return False

        for j in range(9):
            if len([n for n in j if n != 0]) != len(set(board[j])):
                return False
        pass
