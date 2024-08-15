from src.board import Board
import copy


class SudokuSolver:

    def __init__(self, board):
        self.board = board
        self.steps = []

    def solve(self):
        self.steps = []
        self._solve(self.board)
        return self.steps

    def _solve(self, board):
        empty = self.find_empty_location(board)
        if not empty:
            self.steps.append(copy.deepcopy(board))
            return True

        row, col = empty
        for num in range(1, 10):
            board[row][col] = num
            if Board().is_valid_board(board):
                self.steps.append(copy.deepcopy(board))
                if self._solve(board):
                    return True
            board[row][col] = 0
        return False

    def find_empty_location(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None
