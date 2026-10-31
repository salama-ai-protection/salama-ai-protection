
# SALAMA AI - Tableau de bord de démonstration
# Données entièrement fictives

from analyse_donnees import analyser_besoins

donnees_demo = [
    {"ville": "Kinshasa", "besoin": "Soutien psychosocial"},
    {"ville": "Kinshasa", "besoin": "Protection"},
    {"ville": "Bukavu", "besoin": "Protection"},
    {"ville": "Kolwezi", "besoin": "Soutien psychosocial"},
    {"ville": "Bandundu", "besoin": "Assistance juridique"}
]

def afficher_tableau_de_bord():
    resultats = analyser_besoins(donnees_demo)

    print("=== TABLEAU DE BORD SALAMA AI ===")
    print("Données fictives de démonstration")
    print("Total :", resultats["total"])

    print("\nRépartition par ville :")
    for ville, nombre in resultats["par_ville"].items():
        print(f"- {ville} : {nombre}")

    print("\nRépartition par besoin :")
    for besoin, nombre in resultats["par_besoin"].items():
        print(f"- {besoin} : {nombre}")


if __name__ == "__main__":
    afficher_tableau_de_bord()
