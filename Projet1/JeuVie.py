import copy
import time
import random
from tkinter import *

class Grille_jeu_de_la_vie:
    def __init__ (self, lignes,colonnes):
        #Initialisation de la grille avec des dimensions spécifiées
        self.lignes = lignes
        self.colonnes = colonnes
        #Initialisation de la grille avec des cellules mortes
        self.grille = [[0 for i in range(self.colonnes)] for j in range(self.lignes)]
        
    def definir_cellule(self, ligne, colonne, valeur):
        #Methode pour definir la valeur d'une cellule spécifique*
        self.grille[ligne][colonne]=valeur
        
    def obtenir_cellule(self, ligne, colonne):
        #Methode pour obtenir la valeur d'une cellule spécifique
        return self.grille[ligne][colonne]
    
    def randomize(self, densite=0.2):
        #Remplit la grille avec des cellule
        for ligne in range(self.lignes):
            for colonne in range(self.colonnes):
                if random.random()<densite:
                    self.definir_cellule(ligne, colonne, 1) #1 represente une cellule vivante
        
class Jeu_de_la_vie:
    def __init__(self, lignes, colonnes):
        #Initialisation du jeu avec une grille donnée
        self.grille = Grille_jeu_de_la_vie(lignes, colonnes)
        
    def obtenir_voisins(self, ligne, colonne):
        #Methode pour obtenir les coordonnées des voisins d'une cellule
        voisins=[]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i==0 and j==0:
                    continue
                nouvelle_ligne = ligne + i
                nouvelle_colonne= colonne + j
                #Vérification des limites de la grille
                if 0<= nouvelle_ligne < self.grille.lignes and 0<= nouvelle_colonne < self.grille.colonnes:
                    voisins.append((nouvelle_ligne, nouvelle_colonne))
        return voisins
    
    def mettre_a_jour(self):
        #Methode pour mettre a jour l'etat du jeu selon les règles du jeu de la vie
        nouvelle_grille = copy.deepcopy(self.grille)
        
        for ligne in range(self.grille.lignes):
            for colonne in range(self.grille.colonnes):
                cellule = self.grille.obtenir_cellule(ligne,colonne)
                voisins = self.obtenir_voisins(ligne, colonne)
                voisins_vivants = sum(self.grille.obtenir_cellule(l,c) for l, c in voisins)
                
                if cellule ==1 and (voisins_vivants < 2 or voisins_vivants >3):
                    nouvelle_grille.definir_cellule(ligne, colonne, 0) #La cellule meurt
                elif cellule == 0 and voisins_vivants ==3:
                    nouvelle_grille.definir_cellule(ligne, colonne, 1) #Une nouvelle cellule nait
        self.grille = nouvelle_grille
#Fonction pour mettre à jour l'interface graphique
def Mis_a_jour():
    jeu.mettre_a_jour()
    for i in range(lignes):
        for j in range(colonnes):
            if jeu.grille.obtenir_cellule(i, j) == 1:
                couleur = "red"
            else:
                couleur = "white"
            canvas.itemconfig(rectangles[i][j], fill=couleur)
    fenetre.after(1000, Mis_a_jour) #Appel recursif apres 1000 ms(1seconde)
    
#Exemple d'utilisation avec une interface graphique Tkinter
lignes = 10
colonnes = 20
jeu = Jeu_de_la_vie(lignes, colonnes)
jeu.grille.randomize(densite=0.2) #Remplissage aléatoire de la grille

fenetre = Tk()
fenetre.title("Jeu de la vie")

canvas = Canvas(fenetre, width=colonnes * 40, height=lignes *40)
canvas.pack()

rectangles = [[canvas.create_rectangle(j*40, i*40, (j +1 )* 40, (i+1)* 40, outline="black", fill="white") for j in range(colonnes)] for i in range(lignes)]
    
Mis_a_jour() #Démarre la mise àjour de l'interface graphique
fenetre.mainloop()
            