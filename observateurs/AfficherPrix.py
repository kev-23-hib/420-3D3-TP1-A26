import tkinter as tk
from observateurs.observateur import Observateur
from utilitaires import formater_prix


class AfficherPrix(Observateur):

    def __init__(self, parent, titres):
        self.frame = tk.LabelFrame(
            parent,
            text="Prix en temps réel",
            padx=10,
            pady=10
        )
        self.frame.pack(fill="x", padx=20, pady=10)

        self.labels_prix = {}

        for ticker in titres:
            self._creer_ligne(ticker)

    def _creer_ligne(self, ticker):
        ligne = tk.Frame(self.frame)
        ligne.pack(fill="x")

        label_ticker = tk.Label(
            ligne,
            text=ticker,
            width=10
        )
        label_ticker.pack(side="left")

        label_prix = tk.Label(
            ligne,
            text="--"
        )
        label_prix.pack(side="left")

        self.labels_prix[ticker] = label_prix

    def ajouter_titre(self, ticker):
        if ticker not in self.labels_prix:
            self._creer_ligne(ticker)

    def retirer_titre(self, ticker):
        if ticker in self.labels_prix:
            self.labels_prix[ticker].master.destroy()
            del self.labels_prix[ticker]

    def actualiser(self, sujet):
        donnees = sujet.get_donnees()
        titres = donnees["gestion_titre"]
        prix_en_temps_reel = donnees["prix_en_temps_reel"]

        # Supprimer les lignes des titres qui n'existent plus
        for ticker in list(self.frames_prix.keys()):
            if ticker not in titres:
                self.frames_prix[ticker].destroy()
                del self.frames_prix[ticker]
                self.labels_prix.pop(ticker, None)

        # Créer ou mettre à jour les lignes de prix
        for ticker, (prix, ouverture) in prix_en_temps_reel.items():

            if ticker not in self.labels_prix:
                self._creer_ligne(ticker)

            texte, couleur = formater_prix(prix, ouverture)

            self.labels_prix[ticker].config(
                text=texte,
                fg=couleur
            )