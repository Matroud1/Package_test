# Le __main__.py va permet à notre code d'être executable comme un script
# Le point '.' indique un import depuis le même package
from .nettoyage import supprimer_na
from .stats import moyenne, ecart_type
import pandas as pd # pour convertir une liste en dataframe

def main():
    dataset = [1, 2, 3, 5, 8, None, 13, 21, None]
    # conversion en DataFrame pour l'exemple
    dataset_series = pd.Series(dataset)
    print("Nettoyage des données...")
    supp = supprimer_na(dataset_series)
    print("Données nettoyées :", supp)

    print("Calcul de la moyenne...")
    moye = moyenne(norma)
    print("Moyenne :", moye)

    print("Calcul de l'écart type...")
    ecart = ecart_type(norma)
    print("Écart-type :", ecart)

# le if __name=="__main__" fait en sorte que le fichier qui s'execute quand je lance mon script soit celui-ci et pas un autre.
if __name__ == "__main__":
    main()

# main() contient ton code principal.
# Le bloc if __name__ == "__main__": garantit que le code s’exécute uniquement si tu lances ce fichier, pas si tu l’importes ailleurs.