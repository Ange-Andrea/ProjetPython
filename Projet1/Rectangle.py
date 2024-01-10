class Rectangle:
    def __init__(self, largeur, longuer):
        self.__largeur=largeur
        self.__longuer=longuer
    def aire(self):
        print (self.__largeur*self.__longuer)
    def perimetre(self):
        print (2*(self.__largeur+self.__longuer))
    
exemple= Rectangle(3,2)
exemple.aire()
exemple.perimetre()