class Board:
    def __init__(self):
        pass

    def load_board(self):
        file_path = "src/puzzles/dorm.txt"
        with open(file_path, 'r') as file:
            lines = file.readlines()

        board = []
        for line in lines:
            row = list(map(int, line.split()))
            board.append(row)
        
        return board

    def is_valid_subgrid(self, board, row, col, val):
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + startRow][j + startCol] == val:
                    return False
        return True

    def is_valid_board(self, board, row, col, val):
        for j in range(9):
            if board[row][j] == val:
                return False

        for i in range(9):
            if board[i][col] == val:
                return False

        if not self.is_valid_subgrid(board, row, col, val):
            return False

        return True
