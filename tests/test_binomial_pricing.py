import pytest
from math import isclose
from option_pricing.bimodel import BinomialModel
from option_pricing.options import EuropeanCallOption, EuropeanPutOption, AsianCallOption, AsianPutOption, GeometricAsianCallOption, GeometricAsianPutOption

@pytest.mark.parametrize(
    "S0,u,d,r,N,K,expected",
    [(100,0.1,-0.1,0.0,3,130,0.3875),
     (100,0.1,-0.1,0.05,3,130,1.129737609)]
)
def test_european_call_option_pricing(S0,u,d,r,N,K,expected):
    model = BinomialModel(
                spot = S0,
                up = u,
                down = d,
                rate = r,
                n_step = N
            )
    
    option = EuropeanCallOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)

@pytest.mark.parametrize(
    "S0,u,d,r,N,K,expected",
    [(100,0.1,-0.1,0.0,3,130,30.3875),
     (100,0.1,-0.1,0.05,3,130,13.42862542)]
)
def test_european_put_option_pricing(S0,u,d,r,N,K,expected):
    model = BinomialModel(
                spot = S0,
                up = u,
                down = d,
                rate = r,
                n_step = N
            )
    
    option = EuropeanPutOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)

@pytest.mark.parametrize(
    "S0,u,d,r,N,K,expected",
    [(100,0.1,-0.1,0.0,3,130,0),
     (100,0.1,-0.1,0.05,3,130,0)]
)
def test_asian_call_option_pricing(S0,u,d,r,N,K,expected):
    model = BinomialModel(
                spot = S0,
                up = u,
                down = d,
                rate = r,
                n_step = N
            )
    
    option = AsianCallOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)

@pytest.mark.parametrize(
    "S0,u,d,r,N,K,expected",
    [(100,0.1,-0.1,0.0,3,130,30),
     (100,0.1,-0.1,0.05,3,130,16.98520678)]
)
def test_asian_put_option_pricing(S0,u,d,r,N,K,expected):
    model = BinomialModel(
                spot = S0,
                up = u,
                down = d,
                rate = r,
                n_step = N
            )
    
    option = AsianPutOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)

@pytest.mark.parametrize(
    "S0,u,d,r,N,K,expected",
    [(100,0.1,-0.1,0.0,3,110,1.771380157),
     (100,0.1,-0.1,0.05,3,110,4.393955449)]
)
def test_geometric_asian_call_option_pricing(S0,u,d,r,N,K,expected):
    model = BinomialModel(
                spot = S0,
                up = u,
                down = d,
                rate = r,
                n_step = N
            )
    
    option = GeometricAsianCallOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)

@pytest.mark.parametrize(
    "S0,u,d,r,N,K,expected",
    [(100,0.1,-0.1,0.0,3,110,11.99418149),
     (100,0.1,-0.1,0.05,3,110,4.32956158)]
)
def test_geometric_asian_put_option_pricing(S0,u,d,r,N,K,expected):
    model = BinomialModel(
                spot = S0,
                up = u,
                down = d,
                rate = r,
                n_step = N
            )
    
    option = GeometricAsianPutOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)