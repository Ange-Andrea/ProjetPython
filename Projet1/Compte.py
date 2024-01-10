class Compteur:
    nombre_instances = 0  # Attribut de classe pour compter les instances

    def __init__(self):
        Compteur.nombre_instances += 1  # Incrémente le nombre d'instances à chaque création

    @classmethod
    def get_nombre_instances(cls):
        return cls.nombre_instances  # Méthode de classe pour récupérer le nombre d'instances

# Utilisation de la classe Compteur
compteur1 = Compteur()
compteur2 = Compteur()
compteur3 = Compteur()


print("Nombre d'instances :", Compteur.get_nombre_instances())
# Output : Nombre d'instances : 3