from tkinter import *
def afficher_bienvenue(event):
    nom = ENom.get()
    prenom = EPrenom.get()
    LBienvenue.config(text=f"Bienvenue {nom} {prenom}")
     
fenetre=Tk()
fenetre.geometry("400x150")
fenetre.title("Bienvenu")
fenetre.resizable(height=False, width=False)
fenetre.config(background="pink")

LNom= Label(fenetre, text="Nom",padx=10,font=("Arial", 10, "bold"),bg="pink")
LNom.place(x=0, y=10, width=80, height=25)

ENom = Entry(fenetre,font=("Verdona", 10, "italic"))
ENom.place(x=110, y=10, width=200, height=25)
ENom.bind("<Return>", afficher_bienvenue)

LPrenom= Label(fenetre, text="Prenom",padx=10,font=("Arial", 10, "bold"),bg="pink")
LPrenom.place(x=10, y=50, width=80, height=25)

EPrenom = Entry(fenetre,font=("Verdona", 10, "italic"))
EPrenom.place(x=110, y=50, width=200, height=25)
EPrenom.bind("<Return>", afficher_bienvenue)


LBienvenue= Label(fenetre, text="Bienvenue",font=("Arial", 15, "bold"),bg="pink")
LBienvenue.place(x=0, y=90, width=250, height=25)
fenetre.mainloop()

