import tkinter as tk


class SudokuGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Sudoku')
        self.setup_board()
        self.root.mainloop()
        

    def setup_board(self,):
        root = self.root
        frame = tk.Frame(root)
        frame.pack(padx = 20, pady = 20)

        for i in range(0,8):
            for j in range(0,8):
                label = tk.Label(frame, text = 'x',width=3, font=18)
                label.grid(row = i, column = j)
        

        