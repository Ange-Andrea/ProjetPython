import random
import copy
from tkinter import *

class arbre:
    def __init__(self,etat_Arbre=0):
        self.__etat_Arbre= etat_Arbre
    def symbole(self):
        if (self.__etat_Arbre==0):
            return "."
        elif (self.__etat_Arbre==1):
            return "A"
        elif (self.__etat_Arbre==2):
            return "F"
        elif (self.__etat_Arbre==3):
            return "C"
    def set_etat_Arbre(self, a):
            self.__etat_Arbre= a
    def get_etat_Arbre(self):
            return self.__etat_Arbre
class foret:
    def __init__(self,ligne, colonne,densite):
        self.__ligne= ligne
        self.__colonne= colonne
        self.__densite= densite
        self.__grille = [[arbre(0) for i in range (self.__colonne)] for i in range(self.__ligne)]
        
    def init_foret(self):
        for i in range(self.__ligne):
            for j in range(self.__colonne):
                if random.random()<self.__densite:
                    self.__grille[i][j].set_etat_Arbre(1)
        self.__grille[random.randint(0, self.__ligne-1)][random.randint(0, self.__colonne-1)].set_etat_Arbre(2)
        return self.__grille
    
    def affichage_grille(self):
        for ligne in self.__grille:
            for arbre in ligne:
                print (arbre.symbole(), end= " ")
            print()
            
    def voisinage_en_feu(self, x, y):
        if x > 0 and self.__grille[x - 1][y].get_etat_Arbre() ==2:
            return True
        elif x < self.__ligne - 1 and self.__grille[x+1][y].get_etat_Arbre() == 2:
            return True
        elif y > 0 and self.__grille[x][y-1].get_etat_Arbre()==2:
            return True
        elif y < self.__colonne - 1 and self.__grille[x][y+1].get_etat_Arbre() == 2:
            return True
        else:
            return False
        
    def mis_a_jour(self):
        #while self.__densite>0.1:
        nouvelle_grille = copy.deepcopy(self.__grille)
        for i in range(self.__ligne):
            for j in range(self.__colonne):
                etat_actuel = self.__grille[i][j].get_etat_Arbre()
                
                if etat_actuel == 1 and self.voisinage_en_feu(i,j):
                    nouvelle_grille[i][j].set_etat_Arbre(2)
                    
                elif etat_actuel== 2:
                    nouvelle_grille[i][j].set_etat_Arbre(3)
        self.__grille = nouvelle_grille
        return self.__grille
    def proportion(self):
        nbr=0
        for i in range(self.__colonne -1):
            for j in range(self.__ligne-1):
                if self.__grille[i][j].get_etat_Arbre()==1:
                    nbr=nbr+1
        p = nbr/(self.__ligne*self.__colonne)
        print("La proportion d'arbre dans la foret=", p)
        print()
        
        
    def simuler_feu(self, nombre_iteration):
        self.init_foret()
        for _ in range(nombre_iteration):
            print()
            self.affichage_grille()
            print()
            self.proportion()
            print()
            self.mis_a_jour()

    # Classe pour l'interface graphique
class ApplicationSimulationForet:
    
    def __init__(self, root, foret1):
        self.root = root
        self.foret1 = foret1
        self.taille_cellule = 20
        self.canvas = Canvas(self.root, width=foret1._foret__colonne * self.taille_cellule, height=foret1._foret__ligne* self.taille_cellule)
        self.canvas.grid()
        
        #Bouton "Start"
        self.start_bouton = Button(self.root, text="Start", font=('verdena', 10, 'italic'), bg="#6d7270", command=self.start_simulation)
        self.start_bouton.grid(row=1, column=0)
        
    def dessiner_foret(self):
        self.canvas.delete('all')
        for i in range(len(self.foret1._foret__grille)):
            for j in range(len(self.foret1._foret__grille[i])):
                x0 = j* self.taille_cellule
                y0 = i* self.taille_cellule
                x1 = (j+1)* self.taille_cellule
                y1 = (i+1)* self.taille_cellule
                
                etat_cellule = self.foret1._foret__grille[i][j].get_etat_Arbre()
                if etat_cellule == 0:
                    couleur = "white"
                elif etat_cellule == 1:
                    couleur = "green"
                elif etat_cellule == 2:
                    couleur = "red"
                elif etat_cellule == 3:
                    couleur = "gray"
                    
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=couleur)
                
    def start_simulation(self):
        #Initialiser la foret et demarrer la simulation
        self.foret1.init_foret()
        self.dessiner_foret()
        self.root.after(500, self.simulation_step)
        
    def simulation_step(self):
        #Mettre à jour la foret et redessiner
        self.foret1.mis_a_jour()
        self.dessiner_foret()
        
        #Repeter la simulation avec un delai de 500 ms
        self.root.after(500, self.simulation_step)
#Exemple d'utilisation
foret_exemple = foret(20, 20, 0.6)
racine = Tk()
racine.title("Simulation de la propagation d'un feu de foret")
application = ApplicationSimulationForet(racine, foret_exemple)
racine.mainloop()
                    
                    
            
        
          