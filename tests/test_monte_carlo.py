import pytest
from math import isclose

from option_pricing import mcmodel, monte_carlo

@pytest.mark.parametrize(
    "S0,r,sigma,T,step,K,n_sim",
    [(30.0,0.0,0.3,1,3,29.0,1_000)]
)
def test_monte_carlo(S0,r,sigma,T,step,K,n_sim):
    pass

@pytest.mark.parametrize(
    "S0,r,sigma,T,step,K",
    [(30.0,0.0,0.3,1,3,29.0)]
)
def test_european_call_monte_carlo_decreasing_error(S0,r,sigma,T,step,K):
    model = mcmodel.BlackScholesModel(S0, sigma, r, T, step)
    option = monte_carlo.EuropeanCallOption(model, K)
    price_err_list = []
    for n_sim in [10**i for i in range(1,5)]:
        _, price_err = option.get_option_price(n_sim)
        price_err_list.append(price_err)
    
    for i, e in enumerate(price_err_list):
        if i==0: 
            continue
        else:
            assert e < price_err_list[i-1]

@pytest.mark.parametrize(
    "S0,r,sigma,T,step,K",
    [(30.0,0.0,0.3,1,3,29.0)]
)
def test_european_put_monte_carlo_decreasing_error(S0,r,sigma,T,step,K):
    model = mcmodel.BlackScholesModel(S0, sigma, r, T, step)
    option = monte_carlo.EuropeanPutOption(model, K)
    price_err_list = []
    for n_sim in [10**i for i in range(1,5)]:
        _, price_err = option.get_option_price(n_sim)
        price_err_list.append(price_err)
    
    for i, e in enumerate(price_err_list):
        if i==0: 
            continue
        else:
            assert e < price_err_list[i-1]

@pytest.mark.parametrize(
    "S0,r,sigma,T,step,K",
    [(30.0,0.0,0.3,1,3,29.0)]
)
def test_asian_call_monte_carlo_decreasing_error(S0,r,sigma,T,step,K):
    model = mcmodel.BlackScholesModel(S0, sigma, r, T, step)
    option = monte_carlo.AsianCallOption(model, K)
    price_err_list = []
    for n_sim in [10**i for i in range(1,5)]:
        _, price_err = option.get_option_price(n_sim)
        price_err_list.append(price_err)
    
    for i, e in enumerate(price_err_list):
        if i==0: 
            continue
        else:
            assert e < price_err_list[i-1]

@pytest.mark.parametrize(
    "S0,r,sigma,T,step,K",
    [(30.0,0.0,0.3,1,3,29.0)]
)
def test_asian_put_monte_carlo_decreasing_error(S0,r,sigma,T,step,K):
    model = mcmodel.BlackScholesModel(S0, sigma, r, T, step)
    option = monte_carlo.AsianPutOption(model, K)
    price_err_list = []
    for n_sim in [10**i for i in range(1,5)]:
        _, price_err = option.get_option_price(n_sim)
        price_err_list.append(price_err)
    
    for i, e in enumerate(price_err_list):
        if i==0: 
            continue
        else:
            assert e < price_err_list[i-1]

@pytest.mark.parametrize(
    "S0,r,sigma,T,step,K",
    [(30.0,0.0,0.3,1,3,29.0)]
)
def test_geometric_asian_call_monte_carlo_decreasing_error(S0,r,sigma,T,step,K):
    model = mcmodel.BlackScholesModel(S0, sigma, r, T, step)
    option = monte_carlo.GeometricAsianCallOption(model, K)
    price_err_list = []
    for n_sim in [10**i for i in range(1,5)]:
        _, price_err = option.get_option_price(n_sim)
        price_err_list.append(price_err)
    
    for i, e in enumerate(price_err_list):
        if i==0: 
            continue
        else:
            assert e < price_err_list[i-1]

@pytest.mark.parametrize(
    "S0,r,sigma,T,step,K",
    [(30.0,0.0,0.3,1,3,29.0)]
)
def test_geometric_asian_put_monte_carlo_decreasing_error(S0,r,sigma,T,step,K):
    model = mcmodel.BlackScholesModel(S0, sigma, r, T, step)
    option = monte_carlo.GeometricAsianPutOption(model, K)
    price_err_list = []
    for n_sim in [10**i for i in range(1,5)]:
        _, price_err = option.get_option_price(n_sim)
        price_err_list.append(price_err)
    
    for i, e in enumerate(price_err_list):
        if i==0: 
            continue
        else:
            assert e < price_err_list[i-1]
