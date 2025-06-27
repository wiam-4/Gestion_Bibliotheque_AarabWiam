import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def genres_pie(biblio):
    genres = {}
    for livre in biblio.livres.values():
        genres[livre.genre] = genres.get(livre.genre, 0) + 1

    labels = list(genres.keys())
    sizes = list(genres.values())

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des livres par genre")
    plt.axis('equal')  
    plt.show()

def top_auteurs(biblio):
    auteurs = {}
    for livre in biblio.livres.values():
        auteurs[livre.auteur] = auteurs.get(livre.auteur, 0) + 1

    auteurs_tries = sorted(auteurs.items(), key=lambda x: x[1], reverse=True)[:10]
    noms = [a[0] for a in auteurs_tries]
    counts = [a[1] for a in auteurs_tries]

    plt.figure(figsize=(10, 6))
    plt.barh(noms[::-1], counts[::-1], color='skyblue')
    plt.xlabel('Nombre de livres')
    plt.title('Top 10 des auteurs les plus populaires')
    plt.tight_layout()
    plt.show()

def activite_emprunts(biblio):
    today = datetime.today()
    dates = [today - timedelta(days=i) for i in range(30)]
    dates_str = [d.strftime('%Y-%m-%d') for d in dates]

    emprunts_jour = {date:0 for date in dates_str}

    for action in biblio.historique:
        if len(action) < 4:
            continue
        act_type, _, _, date_str = action
        if act_type == "emprunt" and date_str in emprunts_jour:
            emprunts_jour[date_str] += 1

    x = list(emprunts_jour.keys())[::-1]
    y = [emprunts_jour[date] for date in x]

    plt.figure(figsize=(12, 6))
    plt.plot(x, y, marker='o')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Nombre d\'emprunts')
    plt.title('Activité des emprunts sur les 30 derniers jours')
    plt.tight_layout()
    plt.show()
