from observateur import Observateur


class AfficherAlertes(Observateur):

    def __init__(self, label_alertes):
        self.label_alertes = label_alertes

    def actualiser(self, sujet):
        alertes = []

        for ticker, (prix, _) in sujet.prix_en_temps_reel.items():

            titre = sujet.gestion_titre[ticker]

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

