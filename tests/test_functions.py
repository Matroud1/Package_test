import pandas as pd
from monPackage.nettoyage import supprimer_na
from monPackage.stats import moyenne, ecart_type

dataset = pd.Series([1, 2, 3, 5, 8, None, 13, 21, None])

def test_supprimer_na():
    result = supprimer_na(dataset)
    expected = pd.Series([1., 2., 3., 5., 8., 13., 21.])
    pd.testing.assert_series_equal(result.reset_index(drop=True), expected, check_dtype=False)

def test_moyenne():
    series = pd.Series([1, 2, 3])
    assert moyenne(series) == 2.0

def test_ecart_type():
    series = pd.Series([1, 2, 3, 4])
    assert abs(ecart_type(series) - 1.2909944487358056) < 1e-9