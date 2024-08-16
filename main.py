import tkinter as tk
from src.gui import SudokuGUI
from src.board import Board
from src.solver import SudokuSolver


if __name__ == "__main__":
    sudoku_board = Board().load_board()
    testObj = SudokuGUI(sudoku_board)
