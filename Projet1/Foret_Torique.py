class foret_torique(foret):
    #Herite de la class foret
    def voisinage_en_feu(self, x, y):
        voisins=[
            ((x-1)%self._foret__lignes,y),
            ((x+1)%self._foret__lignes,y),
            (x, (y-1)%self._foret__colonne),
            (x, (y-1)%self._foret__colonne),]
        return any(self._foret__grille[i][j].get_etat_Arbre() == 2 for i, j in voisins)