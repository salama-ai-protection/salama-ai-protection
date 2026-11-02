
def orienter_besoin(besoin):
    orientations = {
        "Soutien psychosocial": (
            "Orientation indicative vers un professionnel "
            "qualifié en soutien psychosocial."
        ),
        "Protection": (
            "Orientation indicative vers un service "
            "spécialisé de protection."
        ),
        "Assistance juridique": (
            "Orientation indicative vers un service "
            "d'assistance juridique."
        ),
    }

    return orientations.get(
        besoin,
        "Besoin non reconnu. Une évaluation humaine est nécessaire."
    )
