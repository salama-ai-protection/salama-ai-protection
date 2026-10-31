
# SALAMA AI - Tests automatisés du prototype

import unittest
from analyse_donnees import analyser_besoins


class TestAnalyseDonnees(unittest.TestCase):

    def test_donnees_vides(self):
        resultat = analyser_besoins([])
        self.assertEqual(resultat["total"], 0)
        self.assertEqual(resultat["par_ville"], {})
        self.assertEqual(resultat["par_besoin"], {})

    def test_nombre_total(self):
        donnees = [
            {"ville": "Kinshasa", "besoin": "Protection"},
            {"ville": "Bukavu", "besoin": "Soutien psychosocial"}
        ]
        resultat = analyser_besoins(donnees)
        self.assertEqual(resultat["total"], 2)

    def test_repartition_par_ville_et_besoin(self):
        donnees = [
            {"ville": "Kinshasa", "besoin": "Protection"},
            {"ville": "Kinshasa", "besoin": "Protection"},
            {"ville": "Kolwezi", "besoin": "Soutien psychosocial"}
        ]
        resultat = analyser_besoins(donnees)
        self.assertEqual(resultat["par_ville"]["Kinshasa"], 2)
        self.assertEqual(resultat["par_ville"]["Kolwezi"], 1)
        self.assertEqual(resultat["par_besoin"]["Protection"], 2)


if __name__ == "__main__":
    unittest.main()
