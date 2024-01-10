class duree():
    def __init__(self, s, m, h):
        if s<0 or m<0 or h<0:
            s=abs(s)
            m=abs(m)
            h=abs(h)
        self.__s = s
        self.__m = m
        self.__h = h
    def get_m(self):
        return self.__m
    def set_m (self, a):
        self.__m=a
        
    def conversion(self):
        duree_total=self.__h*3600+self.__m*60+self.__s
        self.__h = duree_total//3600
        self.__m = (duree_total%3600)//60
        self.__s = (duree_total%3600)%60
    def affichage(self):
        print(self.__h, ':', self.__m, ':', self.__s)
    def nombre_total(self):
        return self.__h*3600+self.__m*60+self.__s+self.s
    def ajout(self, seconde):
        self.s= self.__s+seconde
        duree_total=self.__h+3600+self.__m*60+self.s
        self.__h= duree_total//3600
        self.__m= (duree_total%3600)//60
        self.__s= (duree_total%3600)%60
        self.affichage()
        
