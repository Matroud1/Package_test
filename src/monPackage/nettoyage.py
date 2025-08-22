import pandas as pd

def supprimer_na(series: pd.Series) -> pd.Series:
    """Supprime les valeurs manquantes (None ou NaN)"""
    return series.dropna()

