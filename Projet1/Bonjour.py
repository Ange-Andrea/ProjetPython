
# On importe Tkinter
from tkinter import *

fenetre = Tk()
fenetre.geometry("400x100")

champ_label = Label(fenetre, text="Bonjour tout le monde",font=("Arial", 20), fg="red")

champ_label.pack()
bouton_quitter = Button(fenetre, text="Quitter", font=( "Arial", 15), bg= "red",command=fenetre.quit)
bouton_quitter.pack(pady=10)

fenetre.mainloop()