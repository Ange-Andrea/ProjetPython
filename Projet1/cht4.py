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
        self.joueurs = ['Joueur1', 'Joueur2']
        self.joueur_actuel = 0
        self.plateau = [[' ' for _ in range(dimension)] for _ in range(dimension)]
        self.pions_joueur1 = []
        self.pions_joueur2 = []

        self.canvas = tk.Canvas(self.root, width=50*self.dimension, height=50*self.dimension)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click_handler)

        self.cercle = None
        self.derniere_case = None
        self.afficher_plateau()
        self.afficher_joueur_actuel()

    def afficher_plateau(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, outline="black")

    def afficher_joueur_actuel(self):
        joueur_text = f"{self.joueurs[self.joueur_actuel]}'s turn"
        self.root.title(joueur_text)

    def click_handler(self, event):
        row, col = event.y // 50, event.x // 50
        if self.plateau[row][col] == ' ':
            if self.cercle:
                self.canvas.delete(self.cercle)
                self.derniere_case = None

            if self.joueur_actuel == 0:
                couleur = 'blue'
            else:
                couleur = 'red'

            self.cercle = self.canvas.create_oval(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, outline=couleur, width=2)
            self.derniere_case = (row, col)

    def recommencer_partie(self):
        self.canvas.delete("all")
        self.plateau = [[' ' for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.pions_joueur1 = []
        self.pions_joueur2 = []
        self.joueur_actuel = 0
        self.cercle = None
        self.derniere_case = None
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
