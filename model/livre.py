class Livre:
    def __init__(self, isbn, titre, auteur, annee, genre, statut="disponible"):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre
        self.statut = statut

