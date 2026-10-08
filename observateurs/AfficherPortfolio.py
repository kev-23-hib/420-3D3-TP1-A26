import tkinter as tk

from observateurs.observateur import Observateur


class AfficherPortfolio(Observateur):

    def __init__(self, parent):
        self.frame = tk.LabelFrame(
            parent,
            text="Valeur du portefeuille",
            padx=10,
            pady=10
        )
        self.frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.label_valeur = tk.Label(
            self.frame,
            text="Valeur totale : 0.00 $",
            font=("Segoe UI", 13, "bold")
        )
        self.label_valeur.pack(anchor="w")

        self.label_variation = tk.Label(
            self.frame,
            text="▲ 0.00 $ depuis l'ouverture"
        )
        self.label_variation.pack(anchor="w")

    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()

        prix_actuels = donnees["prix_en_temps_reel"]
        titres = donnees["gestion_titre"]
        valeur_totale = donnees["portfolio"]

        valeur_ouverture = sum(
            ouverture * titres[ticker]["quantite"]
            for ticker, (_, ouverture)
            in prix_actuels.items()
        )

        variation_portfolio = (
            valeur_totale - valeur_ouverture
        )

        self.label_valeur.config(
            text=f"Valeur totale : {valeur_totale:.2f} $"
        )

        symbole = (
            "▲"
            if variation_portfolio >= 0
            else "▼"
        )

        self.label_variation.config(
            text=(
                f"{symbole} "
                f"{abs(variation_portfolio):.2f} $ "
                f"depuis l'ouverture"
            ),
            fg=(
                "green"
                if variation_portfolio >= 0
                else "red"
            )
        )