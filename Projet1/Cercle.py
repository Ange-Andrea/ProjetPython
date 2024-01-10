class Cercle:
    pi=3.14159
    def __init__(self, rayon=1, absc=0, ord=0):
        self.__rayon = abs(rayon)
        self.__absc =absc
        self.__ord =ord
    #Les methodes
    def aire(self):
        return (Cercle.pi*(self.__rayon **2))
    def perimetre(self):
        return (2*Cercle.pi*self.__rayon)
    def affiche(self):
        
        print(f"Centre : ({self.__absc}, {self.__ord}), Rayon : {self.__rayon}")

    def coordonnéeInclu(self, abs1, ord1):
        if abs1>=self.__absc-self.__rayon and abs1<=self.__absc+self.__rayon:
            return True
        elif ord1>=self.__ord-self.__rayon and ord1<=self.__ord+self.__rayon:
            return True
        else:
            return False
        
cercle1 = Cercle()
cercle2 = Cercle(2,3,4)
cercle2.affiche()