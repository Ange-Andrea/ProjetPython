import tkinter as tk
from tkinter import messagebox

class GameGUI:
    def __init__(self, root, size=10, marks_to_win=5):
        self.root = root
        self.size = size
        self.marks_to_win = marks_to_win
        self.players = ['X', 'O']
        self.current_player = 0
        self.moves = 0

        self.board_buttons = []
        self.create_board()

    def create_board(self):
        for row in range(self.size):
            button_row = []
            for col in range(self.size):
                button = tk.Button(self.root, text=' ', width=4, height=2, command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.board_buttons.append(button_row)

    def on_click(self, row, col):
        if self.board_buttons[row][col]['text'] == ' ':
            self.board_buttons[row][col]['text'] = self.players[self.current_player]
            self.moves += 1

            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.players[self.current_player]} wins!")
                self.reset_board()
            elif self.is_blocked():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 1 - self.current_player

    def check_winner(self, row, col):
        directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
                      (1, -2), (2, -1), (2, 1), (1, 2)]

        for dr, dc in directions:
            count = 1
            for i in range(1, self.marks_to_win):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < self.size and 0 <= c < self.size and self.board_buttons[r][c]['text'] == self.board_buttons[row][col]['text']:
                    count += 1
                else:
                    break
            if count == self.marks_to_win:
                return True
        return False

    def is_blocked(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board_buttons[row][col]['text'] == ' ':
                    return False
        return True

    def reset_board(self):
        for row in range(self.size):
            for col in range(self.size):
                self.board_buttons[row][col]['text'] = ' '
        self.current_player = 0
        self.moves = 0

def main():
    root = tk.Tk()
    root.title("Knight's Move Game")

    game = GameGUI(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
