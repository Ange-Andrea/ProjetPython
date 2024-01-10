import tkinter as tk
from tkinter import messagebox

class Pion:
    def __init__(self, joueur, position):
        self.joueur = joueur
        self.position = position

class Jeu:
    def __init__(self, root, dimension=10, pions_aligner=5):
        self.root = root
        self.dimension = dimension
        self.pions_aligner = pions_aligner
        self.joueurs = ['X', 'O']
        self.joueur_actuel = 0
        self.plateau = [[' ' for _ in range(dimension)] for _ in range(dimension)]
        self.pions = []

        self.canvas = tk.Canvas(self.root, width=50*self.dimension, height=50*self.dimension)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click_handler)

        self.afficher_plateau()
        self.afficher_joueur_actuel()

    def afficher_plateau(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, outline="black")
                if self.plateau[i][j] != ' ':
                    self.canvas.create_text(j*50+25, i*50+25, text=self.plateau[i][j], font=("Arial", 20))

    def afficher_joueur_actuel(self):
        joueur_text = f"Joueur {self.joueurs[self.joueur_actuel]}'s turn"
        self.root.title(joueur_text)

    def click_handler(self, event):
        row, col = event.y // 50, event.x // 50
        if self.plateau[row][col] == ' ':
            if not self.pions:
                self.placer_pion(row, col)
            else:
                pion = self.pions[-1]
                directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
                if (abs(row - pion.position[0]), abs(col - pion.position[1])) in directions:
                    self.deplacer_pion(row, col)
                else:
                    messagebox.showwarning("Invalid Move", "Choose a valid move")

    def placer_pion(self, row, col):
        pion = Pion(self.joueurs[self.joueur_actuel], (row, col))
        self.pions.append(pion)
        self.plateau[row][col] = pion.joueur
        self.afficher_plateau()
        if self.verifier_victoire(row, col):
            self.afficher_resultat("Victory")
        elif len(self.pions) == self.dimension * self.dimension:
            self.afficher_resultat("Draw")
        else:
            self.joueur_actuel = 1 - self.joueur_actuel
            self.afficher_joueur_actuel()

    def deplacer_pion(self, row, col):
        pion = self.pions[-1]
        self.plateau[pion.position[0]][pion.position[1]] = ' '
        pion.position = (row, col)
        self.plateau[row][col] = pion.joueur
        self.afficher_plateau()
        if self.verifier_victoire(row, col):
            self.afficher_resultat("Victory")
        elif len(self.pions) == self.dimension * self.dimension:
            self.afficher_resultat("Draw")
        else:
            self.joueur_actuel = 1 - self.joueur_actuel
            self.afficher_joueur_actuel()

    def verifier_victoire(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, self.pions_aligner):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < self.dimension and 0 <= c < self.dimension and self.plateau[r][c] == self.plateau[row][col]:
                    count += 1
                else:
                    break
            if count == self.pions_aligner:
                return True
        return False

    def afficher_resultat(self, resultat):
        messagebox.showinfo("Game Over", f"{resultat}! Play again?")
        self.recommencer_partie()

    def recommencer_partie(self):
        self.canvas.delete("all")
        self.plateau = [[' ' for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.pions = []
        self.joueur_actuel = 0
        self.afficher_plateau()
        self.afficher_joueur_actuel()

def main():
    root = tk.Tk()
    root.title("Knight's Move Game")

    dimension = 10  # Choisissez la dimension du plateau
    pions_aligner = 5  # Choisissez le nombre de pions à aligner

    jeu = Jeu(root, dimension, pions_aligner)

    root.mainloop()

if __name__ == "__main__":
    main()
