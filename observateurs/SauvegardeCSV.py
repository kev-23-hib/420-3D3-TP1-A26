from observateur import Observateur
from datetime import datetime


class SauvegardeCSV(Observateur):

    def actualiser(self, sujet):
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("portfolio.csv", "a") as f:

            for ticker, (prix, ouverture) in sujet.prix_en_temps_reel.items():
                f.write(
                    f"{horodatage},{ticker},{prix:.2f},{ouverture:.2f}\n"
                )