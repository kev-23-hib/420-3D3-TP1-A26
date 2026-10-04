#importation des modules nécessaires
from utilitaires import recuperer_prix
from modeles.sujet import Sujet

#titres avec leurs quantités et seuils de prix
TITRES = {
    "AAPL":  {"quantite": 10, "seuil_haut": 200.0, "seuil_bas": 150.0},
    "GOOGL": {"quantite": 5,  "seuil_haut": 160.0, "seuil_bas": 120.0},
    "MSFT":  {"quantite": 8,  "seuil_haut": 430.0, "seuil_bas": 380.0},
}


class Portefeuille(Sujet):

    #attributs de la classe Portefeuille et appel du constructeur de la classe parente Sujet
    def __init__(self):
        super().__init__()
        self.prix_en_temps_reel = {}
        self.gestion_titre = TITRES
        self.portfolio = 0
     

    #actualisation du portefeuille en récupérant les prix en temps réel et en calculant la valeur totale du portefeuille
    def actualiser_portefeuille(self):
        self.portfolio = 0
        for ticket in self.gestion_titre:
        
            titre = self.gestion_titre[ticket]
            quantite = titre["quantite"]


            prix, ouverture = recuperer_prix(ticket)
            self.prix_en_temps_reel[ticket] = (prix, ouverture)
            valeur_titre = prix * quantite
            self.portfolio = self.portfolio + valeur_titre

        self.notifier()

        

    #ajout d'un titre au portefeuille avec ses quantités et seuils de prix
    def ajouter_titre(self, ticket, quantite, seuil_haut, seuil_bas):
        self.gestion_titre[ticket] = {
            "quantite": quantite,
            "seuil_haut": seuil_haut,
            "seuil_bas": seuil_bas
        }
        self.actualiser_portefeuille()
        
        
    #retrait d'un titre du portefeuille
    def retirer_titre(self, ticket):
        if ticket in self.gestion_titre:
            del self.gestion_titre[ticket]
            self.actualiser_portefeuille()
        else:
            print(f"Le titre {ticket} n'existe pas dans le portefeuille.")



    #modification des quantités et seuils de prix d'un titre existant dans le portefeuille
    def modifier_titre(self, ticket, quantite, seuil_haut, seuil_bas):
        if ticket in self.gestion_titre:
            self.gestion_titre[ticket] = {
                "quantite": quantite,
                "seuil_haut": seuil_haut,
                "seuil_bas": seuil_bas
            }
            self.actualiser_portefeuille()
        else:
            print(f"Le titre {ticket} n'existe pas dans le portefeuille.")






    # implementation de la méthode get_donnees pour récupérer les données du portefeuille 
    def get_donnees(self):
        return {
            "prix_en_temps_reel": self.prix_en_temps_reel,
            "gestion_titre": self.gestion_titre,
            "portfolio": self.portfolio,
        }
    