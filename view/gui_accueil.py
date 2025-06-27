from stats.visualisations import genres_pie, top_auteurs, activite_emprunts

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from stats.visualisations import genres_pie, top_auteurs, activite_emprunts
from model.bibliotheque import Bibliotheque

class ApplicationBibliotheque:
    def __init__(self, root):
        self.root = root
        self.root.title("Application Bibliothèque")
        self.root.geometry("900x600")
        self.biblio = Bibliotheque()
        self.biblio.charger()
        self.afficher_page_accueil()

    def nettoyer_fenetre(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def afficher_page_accueil(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="#ffffff")
        frame.pack(fill="both", expand=True)

        # Logo
        logo_path = os.path.join("assets", "logo.png")
        if os.path.exists(logo_path):
            img = Image.open(logo_path).resize((500, 500))
            logo = ImageTk.PhotoImage(img)
            label_logo = tk.Label(frame, image=logo, bg="#ffffff")
            label_logo.image = logo
            label_logo.pack(pady=10)

        tk.Label(frame, text="Bienvenue dans votre Bibliothèque !", font=("Helvetica", 20, "bold"), bg="#ffffff").pack(pady=20)

        tk.Button(frame, text="Commencer", font=("Helvetica", 14), bg="#003BFD", fg="white",
                  command=self.afficher_interface_principale).pack(pady=10)

    def afficher_interface_principale(self):
        self.nettoyer_fenetre()

        self.root.config(bg="white")
 
        cadre_principal = tk.Frame(self.root, bg="white")
        cadre_principal.pack(fill="both", expand=True)
        logo_path = os.path.join("assets", "logo.png")
        if os.path.exists(logo_path):
            img = Image.open(logo_path).resize((350, 350))
            logo = ImageTk.PhotoImage(img)
            label_logo = tk.Label(cadre_principal, image=logo, bg="white")
            label_logo.image = logo
            label_logo.pack(pady=20)

        boutons_frame = tk.Frame(cadre_principal, bg="white")
        boutons_frame.pack(expand=True)

        btn_livres = self.bouton_avec_icone(boutons_frame, " Livres", "books.png", self.afficher_livres)
        btn_livres.pack(pady=5, ipadx=5, ipady=5)

        btn_membres = self.bouton_avec_icone(boutons_frame, " Membres", "members.png", self.afficher_membres)
        btn_membres.pack(pady=5, ipadx=5, ipady=5)

        btn_emprunts = self.bouton_avec_icone(boutons_frame, " Emprunts", "borrow.png", self.afficher_emprunts)
        btn_emprunts.pack(pady=5, ipadx=5, ipady=5)

        btn_stats = self.bouton_avec_icone(boutons_frame, " Statistiques", "stats.png", self.afficher_statistiques)
        btn_stats.pack(pady=5, ipadx=5, ipady=5)

        btn_biblio = self.bouton_avec_icone(boutons_frame, "Gestion de la Bibliothèque", "biblio.png", self.afficher_bibliotheque)
        btn_biblio.pack(pady=5, ipadx=5, ipady=5)

        btn_retour = tk.Button(cadre_principal, text="⬅ Retour", bg="#ffffff", font=("Helvetica", 12), command=self.afficher_page_accueil)
        btn_retour.pack(pady=5)

    def bouton_avec_icone(self, parent, texte, image_nom, commande):
        chemin = os.path.join("assets", image_nom)
        try:
            image = Image.open(chemin).resize((20, 20))
            icone = ImageTk.PhotoImage(image)
        except Exception:
            icone = None
        bouton = tk.Button(parent, text=texte, image=icone if icone else None,
                           compound="left", font=("Helvetica", 14),
                           bg="#ffffff", fg="black", relief="flat", command=commande)
        bouton.image = icone  
        return bouton

    def afficher_livres(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="📚 Liste des Livres", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)

        colonnes = ("ISBN", "Titre", "Auteur", "Année", "Genre", "Statut")
        tableau = ttk.Treeview(frame, columns=colonnes, show="headings")
        for col in colonnes:
            tableau.heading(col, text=col)
            tableau.column(col, width=130)

        for livre in self.biblio.livres.values():
            tableau.insert("", "end", values=(
                livre.isbn, livre.titre, livre.auteur, livre.annee, livre.genre, livre.statut
            ))

        tableau.pack(expand=True, fill="both", padx=20, pady=10)
        tk.Button(frame, text="⬅ Retour", command=self.afficher_interface_principale).pack(pady=10)

    def afficher_membres(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="👤 Liste des Membres", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)

        colonnes = ("ID", "Nom", "Livres Empruntés")
        tableau = ttk.Treeview(frame, columns=colonnes, show="headings")
        for col in colonnes:
            tableau.heading(col, text=col)
            tableau.column(col, width=150)

        for membre in self.biblio.membres.values():
            tableau.insert("", "end", values=(
                membre.id, membre.nom, ", ".join(membre.livres_empruntes)
            ))

        tableau.pack(expand=True, fill="both", padx=20, pady=10)
        tk.Button(frame, text="⬅ Retour", command=self.afficher_interface_principale).pack(pady=10)

    def afficher_emprunts(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="🔄 Historique des Emprunts", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)

        colonnes = ("Action", "ISBN", "ID Membre")
        tableau = ttk.Treeview(frame, columns=colonnes, show="headings")
        for col in colonnes:
            tableau.heading(col, text=col)
            tableau.column(col, width=150)

        for ligne in self.biblio.historique:
            tableau.insert("", "end", values=ligne)

        tableau.pack(expand=True, fill="both", padx=20, pady=10)
        tk.Button(frame, text="⬅ Retour", command=self.afficher_interface_principale).pack(pady=10)

    def afficher_statistiques(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="📊 Statistiques", font=("Helvetica", 25, "bold"), bg="white").pack(pady=10)

        tk.Button(frame, text="📈 Répartition des genres", command=lambda: genres_pie(self.biblio)).pack(pady=10)
        tk.Button(frame, text="🏆 Top 10 des auteurs", command=lambda: top_auteurs(self.biblio)).pack(pady=10)
        tk.Button(frame, text="📅 Activité 30 jours", command=lambda: activite_emprunts(self.biblio)).pack(pady=10)

        tk.Button(frame, text="⬅ Retour", command=self.afficher_interface_principale).pack(pady=20)

    def afficher_bibliotheque(self):
        self.nettoyer_fenetre()
        cadre = tk.Frame(self.root, bg="white")
        cadre.pack(expand=True, fill="both", padx=40, pady=30)

        tk.Label(cadre, text="Gestion de la Bibliothèque", font=("Helvetica", 20, "bold"),
             bg="white", fg="#050E2C", relief="solid", bd=2, padx=10, pady=5).pack(pady=20)

        boutons_frame = tk.Frame(cadre, bg="white")
        boutons_frame.pack()

        boutons = [
            ("➕ Ajouter un Livre", self.afficher_ajouter_livre_formulaire),
            ("❌ Supprimer un Livre", self.afficher_supprimer_livre_formulaire),
            ("👤 Inscrire un Membre", self.afficher_ajouter_membre_formulaire),
            ("❌ Supprimer un Membre", self.afficher_supprimer_membre_formulaire),
            ("📥 Emprunter un Livre", self.afficher_gestion_emprunts),
            ("📤 Rendre un Livre", self.afficher_rendre_livre_formulaire),
            ("💾 Sauvegarder et Quitter", self.quitter_et_sauvegarder)
            ]

        for texte, commande in boutons:
            tk.Button(boutons_frame, text=texte, font=("Helvetica", 13), bg="#e0f0ff", fg="black",
                  relief="raised", width=40, height=2, command=commande).pack(pady=5)

        tk.Button(cadre, text="⬅ Retour", command=self.afficher_interface_principale,
              font=("Helvetica", 12), bg="#f5f5f5").pack(pady=20)

    def afficher_gestion_emprunts(self):
        self.afficher_emprunter_livre_formulaire()



    def sauvegarder_charger(self):
        self.biblio.sauvegarder()
        self.biblio.charger()
        messagebox.showinfo("Info", "Données sauvegardées et rechargées avec succès") 
    def quitter_et_sauvegarder(self):
        self.biblio.sauvegarder()
        self.root.quit()
    
    def afficher_ajouter_livre_formulaire(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(frame, text="➕ Ajouter un Livre", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)

        form_frame = tk.Frame(frame, bg="white")
        form_frame.pack(pady=10)

        champs = {
            "ISBN": tk.StringVar(),
            "Titre": tk.StringVar(),
            "Auteur": tk.StringVar(),
            "Année": tk.StringVar(),
            "Genre": tk.StringVar()
        }

        for i, (label, var) in enumerate(champs.items()):
            tk.Label(form_frame, text=label + " :", font=("Helvetica", 12), bg="white").grid(row=i, column=0, sticky="e", pady=5, padx=5)
            tk.Entry(form_frame, textvariable=var, width=40).grid(row=i, column=1, pady=5, padx=10)
        def enregistrer_livre():
            isbn = champs["ISBN"].get().strip()
            titre = champs["Titre"].get().strip()
            auteur = champs["Auteur"].get().strip()
            annee = champs["Année"].get().strip()
            genre = champs["Genre"].get().strip()
            if not (isbn and titre and auteur and annee and genre):
                messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
                return

            if isbn in self.biblio.livres:
                messagebox.showerror("Erreur", "Ce livre existe déjà.")
                return

            self.biblio.creer_et_ajouter_livre(isbn, titre, auteur, annee, genre)
            self.biblio.sauvegarder()
            messagebox.showinfo("Succès", f"Livre '{titre}' ajouté avec succès.")
            self.afficher_livres()
        tk.Button(frame, text="✅ Enregistrer", font=("Helvetica", 12), bg="#4CAF50", fg="white",
              command=enregistrer_livre).pack(pady=10)

        tk.Button(frame, text="⬅ Retour", command=self.afficher_bibliotheque).pack()
    def afficher_supprimer_livre_formulaire(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="❌ Supprimer un Livre", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)
        isbn_var = tk.StringVar()

        tk.Label(frame, text="ISBN du Livre à supprimer :", bg="white").pack(pady=5)
        tk.Entry(frame, textvariable=isbn_var, width=30).pack(pady=5)

        def supprimer():
            isbn = isbn_var.get()
            try:
                self.biblio.supprimer_livre(isbn)
                self.biblio.sauvegarder()
                messagebox.showinfo("Succès", f"Livre ISBN {isbn} supprimé.")
                self.afficher_bibliotheque()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        tk.Button(frame, text="❌ Supprimer", command=supprimer, bg="#ff4d4d", fg="white").pack(pady=10)
        tk.Button(frame, text="⬅ Retour", command=self.afficher_bibliotheque).pack()

    def afficher_ajouter_membre_formulaire(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="👤 Inscrire un Membre", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)
        id_var = tk.StringVar()
        nom_var = tk.StringVar()

        tk.Label(frame, text="ID du Membre :", bg="white").pack()
        tk.Entry(frame, textvariable=id_var, width=30).pack(pady=5)
        tk.Label(frame, text="Nom du Membre :", bg="white").pack()
        tk.Entry(frame, textvariable=nom_var, width=30).pack(pady=5)

        def enregistrer():
            id_ = id_var.get()
            nom = nom_var.get()
            if not id_ or not nom:
                messagebox.showerror("Erreur", "Tous les champs sont requis.")
                return
            if id_ in self.biblio.membres:
                messagebox.showerror("Erreur", "Ce membre existe déjà.")
                return
            from model.membre import Membre
            self.biblio.enregistrer_membre(Membre(id_, nom))
            self.biblio.sauvegarder()
            messagebox.showinfo("Succès", f"Membre '{nom}' inscrit avec succès.")
            self.afficher_bibliotheque()

        tk.Button(frame, text="✅ Enregistrer", command=enregistrer, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(frame, text="⬅ Retour", command=self.afficher_bibliotheque).pack()

    def afficher_supprimer_membre_formulaire(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="❌ Supprimer un Membre", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)
        id_var = tk.StringVar()

        tk.Label(frame, text="ID du Membre à supprimer :", bg="white").pack(pady=5)
        tk.Entry(frame, textvariable=id_var, width=30).pack(pady=5)

        def supprimer():
            id_ = id_var.get()
            try:
                self.biblio.supprimer_membre(id_)
                self.biblio.sauvegarder()
                messagebox.showinfo("Succès", f"Membre ID {id_} supprimé.")
                self.afficher_bibliotheque()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        tk.Button(frame, text="❌ Supprimer", command=supprimer, bg="#ff4d4d", fg="white").pack(pady=10)
        tk.Button(frame, text="⬅ Retour", command=self.afficher_bibliotheque).pack()

    def afficher_emprunter_livre_formulaire(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(frame, text="📥 Emprunter un Livre", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)

        form_frame = tk.Frame(frame, bg="white")
        form_frame.pack(pady=10)

        livres_disponibles = [livre.isbn for livre in self.biblio.livres.values() if livre.statut == "disponible"]
        membres_disponibles = list(self.biblio.membres.keys())

        isbn_var = tk.StringVar()
        id_membre_var = tk.StringVar()

        if livres_disponibles:
            isbn_var.set(livres_disponibles[0])
        else:
            livres_disponibles = ["Aucun livre disponible"]
            isbn_var.set(livres_disponibles[0])

        if membres_disponibles:
            id_membre_var.set(membres_disponibles[0])
        else:
            membres_disponibles = ["Aucun membre"]
            id_membre_var.set(membres_disponibles[0])

        tk.Label(form_frame, text="📚 Livre (ISBN):", font=("Helvetica", 12), bg="white").grid(row=0, column=0, sticky="e", pady=5, padx=5)
        tk.OptionMenu(form_frame, isbn_var, *livres_disponibles).grid(row=0, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="👤 ID Membre:", font=("Helvetica", 12), bg="white").grid(row=1, column=0, sticky="e", pady=5, padx=5)
        tk.OptionMenu(form_frame, id_membre_var, *membres_disponibles).grid(row=1, column=1, pady=5, padx=10)


        def confirmer_emprunt():
            isbn = isbn_var.get()
            id_membre = id_membre_var.get()

            if isbn == "Aucun livre disponible" or id_membre == "Aucun membre":
                messagebox.showerror("Erreur", "Aucun livre ou membre sélectionné.")
                return

            try:
                self.biblio.emprunter_livre(isbn, id_membre)
                self.biblio.sauvegarder()
                messagebox.showinfo("Succès", f"Le livre {isbn} a été emprunté par le membre {id_membre}.")
                self.afficher_bibliotheque()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        tk.Button(frame, text="✅ Confirmer l'Emprunt", font=("Helvetica", 12), bg="#4CAF50", fg="white",
              command=confirmer_emprunt).pack(pady=10)

        tk.Button(frame, text="⬅ Retour", command=self.afficher_bibliotheque).pack()

    def afficher_rendre_livre_formulaire(self):
        self.nettoyer_fenetre()
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(frame, text="📤 Retourner un Livre", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)

        form_frame = tk.Frame(frame, bg="white")
        form_frame.pack(pady=10)

        membres_disponibles = [m.id for m in self.biblio.membres.values() if m.livres_empruntes]
        membre_var = tk.StringVar()
        livre_var = tk.StringVar()

        if membres_disponibles:
            membre_var.set(membres_disponibles[0])
        else:
            membres_disponibles = ["Aucun membre"]
            membre_var.set(membres_disponibles[0])

        tk.Label(form_frame, text="👤 ID Membre :", font=("Helvetica", 12), bg="white").grid(row=0, column=0, pady=5, padx=5)
        membre_menu = tk.OptionMenu(form_frame, membre_var, *membres_disponibles)
        membre_menu.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(form_frame, text="📚 Livre à rendre :", font=("Helvetica", 12), bg="white").grid(row=1, column=0, pady=5, padx=5)
        livre_menu_widget = tk.OptionMenu(form_frame, livre_var, "")
        livre_menu_widget.grid(row=1, column=1, pady=5, padx=10)

        def mettre_a_jour_livres(*args):
            id_membre = membre_var.get()
            if id_membre in self.biblio.membres:
                livres_empruntes = self.biblio.membres[id_membre].livres_empruntes
            else:
                livres_empruntes = []

            menu = livre_menu_widget["menu"]
            menu.delete(0, "end")

            if livres_empruntes:
                for livre in livres_empruntes:
                    menu.add_command(label=livre, command=tk._setit(livre_var, livre))
                    livre_var.set(livres_empruntes[0])
            else:
                livre_var.set("")
                menu.add_command(label="Aucun livre", command=tk._setit(livre_var, "Aucun livre"))

        membre_var.trace("w", mettre_a_jour_livres)
        mettre_a_jour_livres()

        def confirmer_retour():
            id_membre = membre_var.get()
            isbn = livre_var.get()

            if isbn == "Aucun livre" or not isbn or not id_membre:
                messagebox.showerror("Erreur", "Aucun livre sélectionné ou membre invalide.")
                return
            try:
                self.biblio.retourner_livre(isbn, id_membre)
                self.biblio.sauvegarder()
                messagebox.showinfo("Succès", f"Le livre {isbn} a été retourné par le membre {id_membre}.")
                self.afficher_bibliotheque()
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        tk.Button(frame, text="✅ Confirmer le Retour", font=("Helvetica", 12), bg="#4CAF50", fg="white",
              command=confirmer_retour).pack(pady=10)

        tk.Button(frame, text="⬅ Retour", command=self.afficher_bibliotheque).pack()



    
