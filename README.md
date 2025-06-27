Application de Gestion de Bibliothèque

Réaliser par: AARAB WIAM

Description:

Cette application permet de gérer une bibliothèque avec une interface graphique en Python (Tkinter) :
- Ajouter, supprimer des livres.
- Ajouter, supprimer des membres.
- Emprunter et rendre des livres.
- Visualiser la liste des livres.
- Visualiser la liste des membres.
- Visualiser la liste des emprunts.
- Visualiser lâ€™historique des emprunts.
- Afficher des statistiques (genre, auteurs, activité).

Guide d'installation:

1. Cloner le dépôt ou télécharger l’archive ZIP 

   git clone https://github.com/wiam-4/Gestion_Bibliotheque_AarabWiam.git

   >>> Si vous ne souhaitez pas utiliser Git pour cloner le dépôt, vous pouvez simplement accéder à la page GitHub du projet, cliquer sur le bouton Code, puis choisir Télécharger ZIP afin d’obtenir directement l’archive complète de l’application.

2. Installer les dépendances :

      pip install matplotlib

3. Lancer l'application :

      python main.py

>>> Le fichier 'main.py' est le point d’entrée de l’application.

Exemples d'utilisation:

Une fois l'application lancée ('python main.py'), vous accédez à un menu d'accueil graphique. Voici quelques exemples d'utilisation possibles :

- 📚 **Visualiser la liste des livres**  
  Depuis le menu principal, cliquez sur "📚 Livres" pour afficher la liste des livres disponibles dans la bibliothèque, avec leurs informations (ISBN, titre, auteur, année, genre, statut).

- 👥 **Visualiser la liste des membres**  
  Depuis le menu principal, cliquez sur "👤 Membres" pour afficher la liste des membres inscrits à la bibliothèque. Chaque membre est affiché avec son identifiant (ID), son nom et la liste des livres qu’il a empruntés.

- 🔁 **Visualiser la liste des emprunts**  
  Depuis le menu principal, cliquez sur "🔄 Emprunts" pour consulter l’historique complet des opérations de prêt et de retour de livres.  
Chaque ligne indique :  
  - l’action effectuée (`emprunt` ou `retour`)  
  - l’ISBN du livre concerné  
  - l’ID du membre ayant effectué l’action.

- 📊 **Voir les statistiques**  
  Depuis le menu principal, accédez à *Statistiques* pour visualiser :
  - La répartition des livres par genre (camembert)
  - Le top 10 des auteurs (histogramme)
  - L'activité des emprunts sur 30 jours (courbe)

- ➕ **Ajouter un livre**  
  Depuis la section *Gestion de la bibliothèque*, cliquez sur "➕ Ajouter un Livre", remplissez les champs (ISBN, titre, auteur, année, genre, statut) puis cliquez sur "✅ Enregistrer".

- ❌ **Supprimer un livre**  
  Depuis la section "Gestion de la Bibliothèque", cliquez sur **❌ Supprimer un Livre**.  
  - Entrez l’ISBN du livre à supprimer.  
  - Cliquez sur **❌ Supprimer** pour retirer le livre de la base de données.  

- 👤 **Inscrire un membre**  
  Cliquez sur "👤 Inscrire un Membre", saisissez l'identifiant et le nom du membre, puis validez.

- ❌ **Supprimer un membre**  
  Depuis la section "Gestion de la Bibliothèque", cliquez sur **❌ Supprimer un Membre**.  
  - Saisissez l’ID du membre concerné.  
  - Cliquez sur **❌ Supprimer** pour le retirer de la liste des membres.

- 📥 **Emprunter un livre**  
  Dans "📥 Emprunter un Livre", sélectionnez un livre disponible et un membre enregistré pour réaliser l'emprunt.

- 📤 **Rendre un livre**  
  Depuis la section "Gestion de la Bibliothèque", cliquez sur **📤 Rendre un Livre**.  
  - Sélectionnez l’ISBN du livre et l’ID du membre.  
  - Cliquez sur **✅ Confirmer le Retour**.  
  L'état du livre repassera à **disponible**, et il pourra être emprunté de nouveau.

- 💾 **Sauvegarder et quitter**  
  Cliquez sur "💾 Sauvegarder et Quitter" pour enregistrer les modifications dans les fichiers (txt, CSV).
# Gestion_Bibliotheque_AarabWiam
