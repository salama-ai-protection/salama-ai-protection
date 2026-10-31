
# SALAMA AI - Prototype d'analyse de données
# Données fictives uniquement

from collections import Counter

def analyser_besoins(donnees):
    """Calcule des indicateurs agrégés sans données personnelles."""

    if not donnees:
        return {
            "total": 0,
            "par_ville": {},
            "par_besoin": {}
        }

    villes = Counter(item["ville"] for item in donnees)
    besoins = Counter(item["besoin"] for item in donnees)

    return {
        "total": len(donnees),
        "par_ville": dict(villes),
        "par_besoin": dict(besoins)
    }


# Exemple fictif pour démonstration
donnees_demo = [
    {"ville": "Kinshasa", "besoin": "Soutien psychosocial"},
    {"ville": "Bukavu", "besoin": "Protection"},
    {"ville": "Kolwezi", "besoin": "Soutien psychosocial"},
    {"ville": "Bandundu", "besoin": "Assistance juridique"},
    {"ville": "Kinshasa", "besoin": "Protection"}
]

if __name__ == "__main__":
    resultat = analyser_besoins(donnees_demo)
    print("Résultats SALAMA AI :")
    print(resultat)
