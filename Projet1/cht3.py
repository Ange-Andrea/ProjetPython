from tkinter import *

class Pion:
    def __init__(self, joueur, coordonnees):
        self.joueur = joueur
        self.coordonnees = coordonnees

class Jeu:
    def __init__(self, fenetre, dimension=10, nb_pions=5):
        self.fenetre = fenetre
        self.dimension = dimension
        self.nb_pions = nb_pions
        self.joueurs = ['Joueur1', 'Joueur2']
        self.current_player = 0
        self.pions_joueur1 = []
        self.pions_joueur2 = []
        self.plateau = [[' ' for _ in range(dimension)] for _ in range(dimension)]

        self.canvas = Canvas(self.fenetre, width=50*self.dimension, height=50*self.dimension)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click_handler)

        self.plateau_jeu()
        self.afficher_joueur_courant()

    def afficher_joueur_courant(self):
        text_affiche = f"{self.joueurs[self.current_player]}"
        self.fenetre.title(text_affiche)

    def plateau_jeu(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, outline="black")
                if (i, j) in self.pions_joueur1:
                    self.canvas.create_oval(j*50+10, i*50+10, (j+1)*50-10, (i+1)*50-10, outline='blue', width=2)
                elif (i, j) in self.pions_joueur2:
                    self.canvas.create_oval(j*50+10, i*50+10, (j+1)*50-10, (i+1)*50-10, outline='red', width=2)
                if self.plateau[i][j] == 'X':
                    self.marquer_case(i, j)

    def click_handler(self, event):
        row, col = event.y // 50, event.x // 50
        if self.plateau[row][col] == ' ':
            if self.current_player == 0:
                self.choisir_case(row, col, self.pions_joueur1)
            else:
                self.choisir_case(row, col, self.pions_joueur2)

    def choisir_case(self, row, col, joueur_pions):
        if joueur_pions:
            last_row, last_col = joueur_pions[-1]
            self.plateau[last_row][last_col] = 'X'
            self.marquer_case(last_row, last_col)
        joueur_pions.append((row, col))
        self.plateau[row][col] = 'O'
        self.plateau_jeu()

    def marquer_case(self, row, col):
        color = 'blue' if self.current_player == 0 else 'red'
        self.canvas.create_line(col*50+10, row*50+10, (col+1)*50-10, (row+1)*50-10, fill=color, width=2)
        self.canvas.create_line(col*50+10, (row+1)*50-10, (col+1)*50-10, row*50+10, fill=color, width=2)

def main():
    fenetre = Tk()
    fenetre.title("Jeu Python")
    dimension = 10
    nb_pions = 5
    game = Jeu(fenetre, dimension, nb_pions)
    fenetre.mainloop()

if __name__ == "__main__":
    main()