from random import sample
from tkinter import Tk, Canvas

COLORS=["ivory", "lime green", "red", "gray75"]

def random_forest(p, n):
    units=[(line,col) for col in range(n) for line in range(n)]
    ntrees=int(n**2*p)
    trees=sample(units,ntrees)
    states=[[0]*n for _ in range(n)]
    for (i,j) in trees:
        states[i][j]=1
    return states

def fill_cell(states, line, col):
    A=(unit*col, unit*line)
    B=(unit*(col+1), unit*(line+1))
    state=states[line][col]
    color=COLORS[state]
    cnv.create_rectangle(A, B, fill=color, outline='')

def fill(states):
    n=len(states)
    for line in range(n):
        for col in range(n):
            fill_cell(states, line, col)

p=0.60
n=50
unit=10

# Fenêtre et canevas
root = Tk()
cnv = Canvas(root, width=unit*n, height=unit*n, background="ivory")
cnv.pack()

# Forêt aléatoire
states=random_forest(p, n)

# Plateau dessiné
fill(states)

root.mainloop()



def update_states(states):
    n=len(states)
    to_fire=[]
    for line in range(n):
        for col in range(n):
            if states[line][col]==2:
                states[line][col]=3
                for (i, j) in voisins(n, line, col):
                    if states[i][j]==1:
                        to_fire.append((i, j))
    for (line,col) in to_fire:
        states[line][col]=2

def fill_cell(states, line, col):
        A=(unit*col, unit*line)
        B=(unit*(col+1), unit*(line+1))
        state=states[line][col]
        color=COLORS[state]
        cnv.create_rectangle(A, B, fill=color, outline='')

def fill(states):
    n=len(states)
    for line in range(n):
        for col in range(n):
            fill_cell(states, line, col)

def propagate():
    update_states(states)
    cnv.delete("all")
    fill(states)
    cnv.after(150, propagate)

p=0.62
n=50
unit=10

# Fenêtre et canevas
root = Tk()
cnv = Canvas(root, width=unit*n, height=unit*n, background="ivory")
cnv.pack()

# Forêt aléatoire
states=random_forest(p, n)

i=n//2
j=0
states[i][j]=2

# Plateau dessiné
fill(states)
propagate()

root.mainloop()

