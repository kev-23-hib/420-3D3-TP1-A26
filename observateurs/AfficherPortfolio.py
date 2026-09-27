from observateurs import Observateur


class AfficherPortfolio(Observateur):

    def __init__(self, label_valeur, label_variation):
        self.label_valeur = label_valeur
        self.label_variation = label_variation

    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()
        portfolio = donnees["portfolio"]
        prix_actuels = donnees["prix_en_temps_reel"]
        titres = donnees["gestion_titre"]

        valeur_ouverture = 0

        valeur_totale = sum(
            prix * titres[t]["quantite"]
            for t, (prix, _) in prix_actuels.items()
        )

        valeur_ouverture = sum(
            ouv * titres[t]["quantite"]
            for t, (_, ouv) in prix_actuels.items()
        )

        variation_portfolio = valeur_totale - valeur_ouverture

        self.label_valeur.config(
            text=f"Valeur totale : {valeur_totale:.2f} $"
        )

        symbole = "▲" if variation_portfolio >= 0 else "▼"

        self.label_variation.config(
            text=f"{symbole} {abs(variation_portfolio):.2f} $ depuis l'ouverture",
            fg="green" if variation_portfolio >= 0 else "red",
        )