from tkinter import *
import random
import string
def generate():
    longueur = 16 
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for i in range(longueur))
    EPassword.delete(0, END)  # Efface le contenu actuel du champ de texte
    EPassword.insert(0, mot_de_passe) 
     
fenetre=Tk()
fenetre.geometry("400x150")
fenetre.title("Facto Calculator")
fenetre.resizable(height=False, width=False)
fenetre.config(background="green")

label=Label(fenetre, text="Bienvenue",padx=10, pady=10, font=("Arial", 20, "bold"), fg="black", bg="green")
label.place(x=100,y=10, width=150,height=25)

EPassword = Entry(fenetre, bg="green", fg="black",font=("Arial", 13, "italic"))
EPassword.place(x=7, y=50, width=300, height=25)
button = Button(fenetre, text="Générer",padx=10, pady=10, font=("Arial", 10, "bold"), bg="#00BFFF", command=generate)
button.place(x=300, y=50, width= 80, height=27)
fenetre.mainloop()