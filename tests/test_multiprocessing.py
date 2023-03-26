import pytest
from math import isclose
from option_pricing.bimodel import BinomialModel
from option_pricing.options import EuropeanCallOption, EuropeanPutOption, AsianCallOption, AsianPutOption, GeometricAsianCallOption, GeometricAsianPutOption

@pytest.mark.parametrize(
    "S0,u,d,r,N,K",
    [(100,0.1,-0.1,0.0,10,130),
     (100,0.1,-0.1,0.05,10,130)]
)
def test_european_call_option_pricing(S0,u,d,r,N,K):
    model = BinomialModel(
                spot = S0,
                up = u,
                down = d,
                rate = r,
                n_step = N
            )
    
    option = EuropeanCallOption(model = model, strike = K)

    assert isclose(option.get_option_price(), option.multi_get_option_price())

@pytest.mark.parametrize(
    "S0,u,d,r,N,K",
    [(100,0.1,-0.1,0.0,10,130),
     (100,0.1,-0.1,0.05,10,130)]
)
def test_asian_call_option_pricing(S0,u,d,r,N,K):
    model = BinomialModel(
                spot = S0,
                up = u,
                down = d,
                rate = r,
                n_step = N
            )
    
    option = AsianCallOption(model = model, strike = K)
    assert isclose(option.get_option_price(), option.multi_get_option_price())
