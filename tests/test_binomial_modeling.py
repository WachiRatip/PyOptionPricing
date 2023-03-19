import pytest
from math import isclose
from option_pricing.bimodel import BinomialModel

@pytest.mark.parametrize(
    "S0,u,d,r,N",
    [(100,0.1,-0.1,0.0,3),
     (100,0.1,-0.1,0.05,3)]
)
def test_option_modeling(S0,u,d,r,N):
    model = BinomialModel(
        spot=S0,
        up=u,
        down=d,
        rate=r,
        n_step=N
    )
    total_prob = 0
    previous_path = None
    previous_prices = None
    for x in range(model.total_path):
        model.get_path(x)
        model.get_path_prices()
        _prob = model.get_path_prob()
        total_prob += _prob
        _path = model.path
        _price = model.prices
        assert len(_path)==model.n_step
        assert len(_price)==model.n_step
        for idx, val in enumerate(_path):
            # val = 1 if up otherwise 0
            if (idx==0):
                if (val==1):
                    assert S0<_price[idx]
                else:
                    assert S0>_price[idx]
            else:
                if (val==1):
                    assert _price[idx-1]<_price[idx]
                else:
                    assert _price[idx-1]>_price[idx]
        
        # check path/price not the same
        current_path = _path
        current_prices = _price
        if previous_path:
            assert (current_path != previous_path)
            assert (current_prices != previous_prices)
        previous_path = _path
        previous_path = _price
        model.clear_path()
    
    assert isclose(total_prob, 1.0)

@pytest.mark.parametrize(
    "S0,u,d,r,N",
    [(100,0.1,-0.1,0.0,3),
     (100,0.1,-0.1,0.05,3)]
)
def test_get_price(S0,u,d,r,N):
    model = BinomialModel(
        spot=S0,
        up=u,
        down=d,
        rate=r,
        n_step=N
    )
    for x in range(model.total_path):
        model.get_path(x)
        model.get_path_prices()
        for i, price in enumerate(model.prices):
            assert model.get_price(x, i)==price

        model.clear_path()

@pytest.mark.parametrize(
    "S0,sigma,m_time,r,N",
    [(100,0.3,1,0.0,3),
     (100,0.3,1,0.05,3)]
)
def test_option_modeling_volatility_m_time(S0,sigma,m_time,r,N):
    model = BinomialModel(
        spot=S0,
        sigma=sigma,
        rate=r,
        m_time=m_time,
        n_step=N
    )
    total_prob = 0
    previous_path = None
    previous_prices = None
    for x in range(model.total_path):
        model.get_path(x)
        model.get_path_prices()
        _prob = model.get_path_prob()
        total_prob += _prob
        _path = model.path
        _price = model.prices
        assert len(_path)==model.n_step
        assert len(_price)==model.n_step
        for idx, val in enumerate(_path):
            # val = 1 if up otherwise 0
            if (idx==0):
                if (val==1):
                    assert S0<_price[idx]
                else:
                    assert S0>_price[idx]
            else:
                if (val==1):
                    assert _price[idx-1]<_price[idx]
                else:
                    assert _price[idx-1]>_price[idx]
        
        # check path/price not the same
        current_path = _path
        current_prices = _price
        if previous_path:
            assert (current_path != previous_path)
            assert (current_prices != previous_prices)
        previous_path = _path
        previous_path = _price
        model.clear_path()
    
    assert isclose(total_prob, 1.0)

@pytest.mark.parametrize(
    "S0,sigma,m_time,r,N",
    [(100,0.3,1,0.0,3),
     (100,0.3,1,0.05,3)]
)
def test_get_price_volatility_m_time(S0,sigma,m_time,r,N):
    model = BinomialModel(
        spot=S0,
        sigma=sigma,
        rate=r,
        m_time=m_time,
        n_step=N
    )
    for x in range(model.total_path):
        model.get_path(x)
        model.get_path_prices()
        for i, price in enumerate(model.prices):
            assert model.get_price(x, i)==price

        model.clear_path()