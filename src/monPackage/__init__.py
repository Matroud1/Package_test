# le fichier __init__.py va permeettre à mon dossier d'être importable comme un packge. En claire, il fait de mon dossier un package.
# Le point '.' indique un import depuis le même package
from .nettoyage import supprimer_na
from .stats import moyenne, ecart_type

# On définit ce qui est accessible directement
__all__ = ["supprimer_na", "moyenne", "ecart_type"]
