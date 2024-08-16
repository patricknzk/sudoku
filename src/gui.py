import tkinter as tk
from src.solver import SudokuSolver


class SudokuGUI:

    def __init__(self, board):
        self.root = tk.Tk()
        self.root.title('Sudoku')
        self.board = board
        self.entries = []
        self.setup_board()
        self.root.mainloop()
        
    def setup_board(self):
        root = self.root
        frame = tk.Frame(root)
        frame.pack(padx=20, pady=20)

        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(frame, width=2, font=18)
                entry.grid(row=i, column=j)

                if self.board[i][j] != 0:
                    entry.insert(0, str(self.board[i][j]))
                    entry.config(state='disabled')
                else:
                    entry.bind('<Return>', lambda event, row=i,
                               col=j: self.user_input(event, row, col))

                row_entries.append(entry)
            self.entries.append(row_entries)

        solve_button = tk.Button(frame, text="Solve", command=self.solve_and_refresh)
        solve_button.grid(row=9, column=0, columnspan=9)

    def refresh_board(self):
        for i in range(9):
            for j in range(9):
                entry = self.entries[i][j]
                entry.config(state='normal')
                entry.delete(0, tk.END)
                if self.board[i][j] != 0:
                    entry.insert(0, str(self.board[i][j]))
                    entry.config(state='disabled')
                else:
                    entry.config(state='normal')

    def solve_and_refresh(self):
        solver = SudokuSolver(self.board)
        steps = solver.solve()
        if steps:
            self.animate_solution(steps)
        else:
            print("No solution exists")

    def animate_solution(self, steps):
        self.steps = steps
        self.current_step = 0
        self.update_board()

    def update_board(self):
        if self.current_step < len(self.steps):
            self.board = self.steps[self.current_step]
            self.refresh_board()
            self.current_step += 1
            self.root.after(1, self.update_board)