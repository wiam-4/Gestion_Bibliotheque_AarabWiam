from datetime import datetime

import json, csv, os
from model.livre import Livre
from model.membre import Membre
from model.exceptions import *

class Bibliotheque:
    def __init__(self):
        self.livres = {}
        self.membres = {}
        self.historique = []

    def ajouter_livre(self, livre):
        self.livres[livre.isbn] = livre
    def creer_et_ajouter_livre(self, isbn, titre, auteur, annee, genre):
        if isbn in self.livres:
            raise Exception("Le livre existe déjà.")
        nouveau_livre = Livre(isbn, titre, auteur, annee, genre, statut="disponible")
        self.ajouter_livre(nouveau_livre)
    def supprimer_livre(self, isbn):
        if isbn in self.livres:
            del self.livres[isbn]
        else:
            raise Exception("Livre introuvable.")

    def enregistrer_membre(self, membre):
        self.membres[membre.id] = membre
    def supprimer_membre(self, id_membre):
        if id_membre in self.membres:
            del self.membres[id_membre]
        else:
            raise Exception("Membre introuvable.")

    def emprunter_livre(self, isbn, id_membre):
        if isbn not in self.livres:
            raise LivreInexistantError()
        if id_membre not in self.membres:
            raise MembreInexistantError()
        livre = self.livres[isbn]
        if livre.statut != "disponible":
            raise LivreIndisponibleError()
        membre = self.membres[id_membre]
        if len(membre.livres_empruntes) >= 3:
            raise QuotaEmpruntDepasseError()
        livre.statut = "emprunté"
        membre.livres_empruntes.append(isbn)
        self.historique.append(["emprunt", isbn, id_membre, datetime.now().strftime('%Y-%m-%d')])

    def retourner_livre(self, isbn, id_membre):
        if isbn not in self.livres or id_membre not in self.membres:
            raise Exception("Livre ou membre inexistant")
        livre = self.livres[isbn]
        membre = self.membres[id_membre]
        if isbn in membre.livres_empruntes:
            membre.livres_empruntes.remove(isbn)
            livre.statut = "disponible"
            self.historique.append(["retour", isbn, id_membre])

    def sauvegarder(self):
        with open("data/livres.txt", "w", encoding="utf-8") as f:
            for livre in self.livres.values():
                f.write(f"{livre.isbn};{livre.titre};{livre.auteur};{livre.annee};{livre.genre};{livre.statut}\n")

        with open("data/membres.txt", "w", encoding="utf-8") as f:
            for membre in self.membres.values():
                livres = ",".join(membre.livres_empruntes)
                f.write(f"{membre.id};{membre.nom};{livres}\n")

        with open("data/historique.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(self.historique)

    def charger(self):
        if os.path.exists("data/livres.txt"):
            with open("data/livres.txt", encoding="utf-8") as f:
                for ligne in f:
                    isbn, titre, auteur, annee, genre, statut = ligne.strip().split(";")
                    self.livres[isbn] = Livre(isbn, titre, auteur, annee, genre, statut)

        if os.path.exists("data/membres.txt"):
            with open("data/membres.txt", encoding="utf-8") as f:
                for ligne in f:
                    parts = ligne.strip().split(";")
                    id_ = parts[0]
                    nom = parts[1]
                    livres_empruntes = parts[2].split(",") if len(parts) > 2 and parts[2] else []
                    self.membres[id_] = Membre(id_, nom, livres_empruntes)

        if os.path.exists("data/historique.csv"):
            with open("data/historique.csv", encoding="utf-8") as f:
                reader = csv.reader(f)
                self.historique = list(reader)



   