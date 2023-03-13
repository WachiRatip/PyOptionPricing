import itertools
import statistics
from math import isclose

import pytest

from option_pricing import mcmodel, monte_carlo


def test_gen_std_normal_rv():
    rv = []
    for _ in itertools.repeat(None, 100_000):
        _rv = mcmodel.get_rv_std_normal()
        rv.append(_rv)
    
    avg = statistics.mean(rv)
    std = statistics.stdev(rv)
    assert isclose(avg, 0.0, abs_tol=5e-2)
    assert isclose(std, 1.0, abs_tol=5e-2)

@pytest.mark.parametrize(
    "S0,r,sigma,T,step,n_sim",
    [(30.0,0.0,0.3,1,3,1_000)]
)
def test_monte_carlo_sample_path(S0,r,sigma,T,step,n_sim):
    model = mcmodel.BlackScholesModel(S0, sigma, r, T, step)
    previous_path = None
    for _ in itertools.repeat(None, n_sim):
        model.get_sample_path()
        current_path = model.prices
        if previous_path:
            assert (current_path != previous_path)
        previous_path = model.prices
        model.clear_path()

@pytest.mark.parametrize(
    "S0,r,sigma,T,step,K",
    [(30.0,0.0,0.3,1,3,29.0)]
)
def test_european_call_monte_carlo_decreasing_error(S0,r,sigma,T,step,K):
    model = mcmodel.BlackScholesModel(S0, sigma, r, T, step)
    option = monte_carlo.EuropeanCallOption(model, K)
    price_err_list = []
    for n_sim in [10**i for i in range(2,5)]:
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
    for n_sim in [10**i for i in range(2,5)]:
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
    for n_sim in [10**i for i in range(2,5)]:
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
    for n_sim in [10**i for i in range(2,5)]:
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
    for n_sim in [10**i for i in range(2,5)]:
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
    for n_sim in [10**i for i in range(2,5)]:
        _, price_err = option.get_option_price(n_sim)
        price_err_list.append(price_err)
    
    for i, e in enumerate(price_err_list):
        if i==0: 
            continue
        else:
            assert e < price_err_list[i-1]
