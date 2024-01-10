from tkinter import *
from Enonce1 import *

COLORS=["ivory", "lime green", "red", "gray75"]
fenetre=Tk()
fenetre.geometry("450x450")
fenetre.title("Foret")
fenetre.resizable(height=False, width=False)
fenetre.config(background="pink")


def propagate():
# Crée un canevas pour dessiner les arbres
    taille_carre = 20
    taille_foret = 20
    canevas = Canvas(fenetre, width=taille_carre*taille_foret, height=taille_carre*taille_foret)
    canevas.pack()

    # Dessine des carrés pour chaque arbre dans la forêt
    for i in range(taille_foret):
        for j in range(taille_foret):
            x1 = i * taille_carre
            y1 = j * taille_carre
            x2 = x1 + taille_carre
            y2 = y1 + taille_carre
            canevas.create_rectangle(x1, y1, x2, y2, fill='green')
            
    
        
button = Button(fenetre, text="Start",padx=10, pady=10, font=("Arial", 10, "bold"), bg="#00BFFF",command=propagate )
button.place(x=80, y=400, width= 80, height=50)

button1 = Button(fenetre, text="Stop",padx=10, pady=10, font=("Arial", 10, "bold"), bg="#00BFFF")
button1.place(x=280, y=400, width= 80, height=50)
fenetre.mainloop()