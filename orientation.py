"""Orientations pédagogiques, non vérifiées et sans données personnelles."""

VILLES = ("Kinshasa", "Bukavu", "Kolwezi", "Bandundu")
BESOINS = ("Soutien psychosocial", "Protection", "Assistance juridique")

CONSEILS = {
    "Soutien psychosocial": (
        "Rechercher un professionnel qualifié en soutien psychosocial ou un service de santé adapté.",
        "Ne pas partager d'informations sensibles dans cette démonstration."
    ),
    "Protection": (
        "Rechercher un service local de protection compétent et un accompagnement confidentiel.",
        "En cas de danger immédiat, se mettre en sécurité et contacter les services d'urgence locaux disponibles."
    ),
    "Assistance juridique": (
        "Rechercher un service d'aide juridique ou une organisation d'accompagnement qualifiée.",
        "Demander des informations sur la confidentialité et les démarches avant de partager des documents."
    ),
}


def orienter_besoin(besoin, ville=None):
    """Retourne un message indicatif; compatible avec l'appel V3 à un seul argument."""
    if besoin not in BESOINS:
        return "Type de besoin non reconnu. Sélectionnez une catégorie proposée."
    if ville is not None and ville not in VILLES:
        return "Ville non reconnue. Sélectionnez une ville proposée."
    intro = f"À {ville}, " if ville else ""
    conseil, precaution = CONSEILS[besoin]
    return (
        f"{intro}orientation indicative pour « {besoin} » : {conseil} "
        f"{precaution} Aucun organisme ni contact local n'a été vérifié pour ce prototype."
    )
