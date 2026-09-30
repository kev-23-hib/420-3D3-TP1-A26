import tkinter as tk
from observateurs.observateur import Observateur


class AfficherAlertes(Observateur):

    def __init__(self, parent):
        self.frame = tk.LabelFrame(
            parent,
            text="Alertes",
            padx=10,
            pady=10
        )
        self.frame.pack(fill="x", padx=20, pady=10)

        self.label_alertes = tk.Label(
            self.frame,
            text="Aucune alerte",
            fg="gray",
            justify="left"
        )
        self.label_alertes.pack(anchor="w")

    def actualiser(self, sujet):
        donnees = sujet.get_donnees()

        prix_en_temps_reel = donnees["prix_en_temps_reel"]
        gestion_titre = donnees["gestion_titre"]

        alertes = []

        for ticker, (prix, _) in prix_en_temps_reel.items():

            titre = gestion_titre[ticker]

            if prix >= titre["seuil_haut"]:
                alertes.append(
                    f"⚠️ {ticker} dépasse le seuil haut "
                    f"({prix:.2f} $ ≥ {titre['seuil_haut']:.2f} $)"
                )

            elif prix <= titre["seuil_bas"]:
                alertes.append(
                    f"⚠️ {ticker} sous le seuil bas "
                    f"({prix:.2f} $ ≤ {titre['seuil_bas']:.2f} $)"
                )

        self.label_alertes.config(
            text="\n".join(alertes) if alertes else "Aucune alerte",
            fg="red" if alertes else "gray"
        )