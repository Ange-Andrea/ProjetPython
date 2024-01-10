from tkinter import *

def afficher_touche(event):
    touche = event.keysym
    label_touche.config(text=f" {touche}")

fenetre = Tk()
fenetre.geometry("400x150")
fenetre.title("Clavier")
fenetre.resizable(height=False, width=False)
fenetre.config(background="pink")

# Label pour afficher la touche du clavier
label_touche = Label(fenetre, text="Appuyez une touche",font=("Arial", 11, "bold"))
label_touche.pack()
label_touche.place(x=100, y=50, width=150, height=35)

# Liaison de l'événement clavier à la fonction afficher_touche
fenetre.bind("<Key>", afficher_touche)

fenetre.mainloop() 