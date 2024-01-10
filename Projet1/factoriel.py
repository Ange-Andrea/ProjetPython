from tkinter import *
def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1);
def calculate():
    result=factorial(int(EvaleurN.get()))
    EFacto.delete(0, END)
    EFacto.insert(0, int(result))
    EFacto.config(text=result)
def effacer():
    champs_texte = [EFacto,EvaleurN]  
    for champ in champs_texte:
        champ.delete(0, END)
fenetre=Tk()
fenetre.geometry("400x150")
fenetre.title("Facto Calculator")
fenetre.resizable(height=False, width=False)
fenetre.config(background="#00BFFF")

valeurN = Label(fenetre, text="Entrez la valeur de n :",padx=10, pady=10, font=("Arial", 10, "bold"), bg="#00BFFF")
valeurN.grid(row=0, column=0)

EvaleurN = Entry(fenetre, width=35)
EvaleurN.grid(row=0, column=1, padx=10)

Lfacto = Label(fenetre, text="Le Factoriel  de n :",padx=10,font=("Arial", 10, "bold"),bg="#00BFFF")
Lfacto.grid(row=1, column=0)

EFacto = Entry(fenetre, width=35)
EFacto.grid(row=1, column=1,padx=10 )
bouton=Button(fenetre, text="Calculer", font=("Verdana", 10, "italic"),command=calculate)
bouton.grid(row=2, column=0, pady=30)
bouton=Button(fenetre, text="Effacer", font=("Verdana", 10, "italic"),command=effacer)
bouton.grid(row=2, column=1, pady=30)
fenetre.mainloop()