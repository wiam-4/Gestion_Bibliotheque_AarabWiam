class Membre:
    def __init__(self, id, nom, livres_empruntes=None):
        self.id = id
        self.nom = nom
        self.livres_empruntes = livres_empruntes if livres_empruntes else []

   