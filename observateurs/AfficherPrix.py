from observateurs import Observateur
from app import formater_prix

class AfficherPrix(Observateur):

    def __init__(self, labels_prix):
        self.labels_prix = labels_prix

    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()
        prix_en_temps_reel = donnees["prix_en_temps_reel"]
        for ticket in prix_en_temps_reel:
            prix, ouverture = prix_en_temps_reel[ticket]
            texte, couleur = formater_prix(prix, ouverture)
            self.labels_prix[ticket].config(text=texte, fg=couleur)


