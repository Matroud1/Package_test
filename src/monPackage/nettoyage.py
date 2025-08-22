
def nettoyer_texte(texte: str) -> str:
    """Nettoie un texte en supprimant espaces inutiles"""
    return " ".join(texte.split())
