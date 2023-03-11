import pytest
from math import isclose
from option_pricing.trimodel import TrinomialModel
from option_pricing.options import EuropeanCallOption, EuropeanPutOption, AsianCallOption, AsianPutOption

@pytest.mark.parametrize(
    "S0,sigma,r,T,N,K,expected",
    [(30,0.3,0.0,1.0,3,29,4.038297683),
     (30,0.3,0.05,1.0,3,29,4.316841094)]
)
def test_european_call_option_pricing(S0,sigma,r,T,N,K,expected):
    model = TrinomialModel(
                spot = S0,
                sigma = sigma,
                rate= r,
                m_time = T,
                n_step = N
            )
    
    option = EuropeanCallOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)

@pytest.mark.parametrize(
    "S0,sigma,r,T,N,K,expected",
    [(30,0.3,0.0,1.0,3,29,3.034898872),
     (30,0.3,0.05,1.0,3,29,2.128036039)]
)
def test_european_put_option_pricing(S0,sigma,r,T,N,K,expected):
    model = TrinomialModel(
                spot = S0,
                sigma = sigma,
                rate= r,
                m_time = T,
                n_step = N
            )
    
    option = EuropeanPutOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)

@pytest.mark.parametrize(
    "S0,sigma,r,T,N,K,expected",
    [(30,0.3,0.0,1.0,3,29,3.133362605),
     (30,0.3,0.05,1.0,3,29,3.260117193)]
)
def test_asian_call_option_pricing(S0,sigma,r,T,N,K,expected):
    model = TrinomialModel(
                spot = S0,
                sigma = sigma,
                rate= r,
                m_time = T,
                n_step = N
            )
    
    option = AsianCallOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)

@pytest.mark.parametrize(
    "S0,sigma,r,T,N,K,expected",
    [(30,0.3,0.0,1.0,3,29,2.131096759),
     (30,0.3,0.05,1.0,3,29,1.517861581)]
)
def test_asian_put_option_pricing(S0,sigma,r,T,N,K,expected):
    model = TrinomialModel(
                spot = S0,
                sigma = sigma,
                rate= r,
                m_time = T,
                n_step = N
            )
    
    option = AsianPutOption(model = model, strike = K)
    assert isclose(option.get_option_price(), expected)
