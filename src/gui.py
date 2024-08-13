import tkinter as tk


class SudokuGUI:

    def __init__(self, board):
        self.root = tk.Tk()
        self.root.title('Sudoku')
        self.setup_board(board)
        self.root.mainloop()
        
    def setup_board(self, board):
        root = self.root
        frame = tk.Frame(root)
        frame.pack(padx=20, pady=20)

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(frame, width=2, font=18)
                entry.grid(row=i, column=j)

                if board[i][j] != 0:
                    entry.insert(0, board[i][j])
                    entry.config(state='disabled')
