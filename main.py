import tkinter as tk
from tkinter import messagebox
from view.gui_accueil import ApplicationBibliotheque
import os
from PIL import Image, ImageTk
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "assets")

UTILISATEURS = {
    "admin": "user",
    "user": "user"
}

def verifier_connexion(username, password, fenetre_connexion):
    if username in UTILISATEURS and UTILISATEURS[username] == password:
        fenetre_connexion.destroy()
        lancer_app()
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

def afficher_connexion():
    login = tk.Tk()
    login.title("Connexion - Bibliothèque")
    login.geometry("400x400")
    login.config(bg="#ffffff") 

    # Logo
    logo_path = os.path.join(ASSETS_PATH, "logo.png")
    if os.path.exists(logo_path):
        img = Image.open(logo_path).resize((120, 120))
        logo = ImageTk.PhotoImage(img)
        label_logo = tk.Label(login, image=logo, bg="#ffffff")
        label_logo.image = logo
        label_logo.pack(pady=15)

    # Titre
    tk.Label(login, text="🔒 Connexion", font=("Helvetica", 18, "bold"), bg="#ffffff").pack(pady=10)

    # Champs de saisie
    tk.Label(login, text="Nom d'utilisateur :", bg="#ffffff", font=("Helvetica", 12)).pack()
    entry_user = tk.Entry(login, font=("Helvetica", 12))
    entry_user.pack(pady=5)

    tk.Label(login, text="Mot de passe :", bg="#ffffff", font=("Helvetica", 12)).pack()
    entry_pass = tk.Entry(login, show="*", font=("Helvetica", 12))
    entry_pass.pack(pady=5)

    # Bouton
    tk.Button(login, text="Se connecter", font=("Helvetica", 12, "bold"),
              bg="#006EFF", fg="white", width=20,
              command=lambda: verifier_connexion(entry_user.get(), entry_pass.get(), login)).pack(pady=20)

    login.mainloop()


def lancer_app():
    root = tk.Tk()
    app = ApplicationBibliotheque(root)
    root.mainloop()

if __name__ == "__main__":
    afficher_connexion()
