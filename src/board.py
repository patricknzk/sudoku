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

    def is_valid_subgrid(self, board):
        # Check all 3x3 subgrids
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                subgrid = []
                for i in range(3):
                    for j in range(3):
                        val = board[start_row + i][start_col + j]
                        if val != 0:
                            subgrid.append(val)
                if len(subgrid) != len(set(subgrid)):
                    return False
        return True

    def is_valid_board(self, board):
        # for the value in a cell, the entire row and entire column cannot
        # contain the same value.
        for i in range(9):
            row = [n for n in board[i] if n != 0]
            if len(row) != len(set(row)):
                return False

        for j in range(9):
            column = [board[i][j] for i in range(9) if board[i][j] != 0]
            if len(column) != len(set(column)):
                return False

        if not self.is_valid_subgrid(board):
            return False

        return True
