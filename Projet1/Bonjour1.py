from tkinter  import *
from tkinter import messagebox
def quitter():
    box=messagebox.askquestion('Quitter','voulez-vous vraiment quitter?', icon='warning')
    if box=='yes':
        fenetre.quit()
fenetre=Tk()
fenetre.geometry("400x150")
fenetre.title("Ma premiere application python")
fenetre.resizable(height=False, width=False)
fenetre.config(background="#00BFFF")

Titre= Label(fenetre, text="Bonjour tout le monde", font=("verdena", 25, "italic"), bg="#00BFFF", fg="white")
Titre.grid(row=0, column=0)
bouton=Button(fenetre, text="Quitter", font=("Verdana", 10, "italic"), command=quitter)
bouton.grid(row=1, column=0, pady=20)
fenetre.mainloop()