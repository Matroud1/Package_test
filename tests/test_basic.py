
from monPackage.nettoyage import nettoyer_texte
from monPackage.stats import moyenne

def test_nettoyer_texte():
    assert nettoyer_texte("Bonjour   le   monde") == "Bonjour le monde"

def test_moyenne():
    assert moyenne([1, 2, 3]) == 2
