import pandas as pd

def moyenne(series: pd.Series) -> float:
    return series.mean()

def ecart_type(series: pd.Series) -> float:
    return series.std()

