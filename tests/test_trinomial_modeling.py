import pytest
from math import isclose
from option_pricing.trimodel import TrinomialModel

@pytest.mark.parametrize(
    "S0,sigma,r,T,N",
    [(100,0.3,0.0,1.0,3),
     (100,0.3,0.05,1.0,3)]
)
def test_option_modeling(S0,sigma,r,T,N):
    model = TrinomialModel(
        spot = S0,
        sigma= sigma,
        rate = r,
        m_time= T,
        n_step = N
    )
    total_prob = 0
    for x in range(model.path_based_number**model.n_step):
        model.get_path(x)
        model.get_path_prices()
        _prob = model.get_path_prob()
        total_prob += _prob
        _path = model.path
        _price = model.prices
        assert len(_path)==model.n_step
        assert len(_price)==model.n_step
        for idx, val in enumerate(_path):
            # val = 2 if up, val = 1 if neutral, otherwise 0
            if (idx==0):
                if (val==2):
                    assert S0<_price[idx]
                elif (val==1):
                    assert S0==_price[idx]
                else:
                    assert S0>_price[idx]
            else:
                if (val==2):
                    assert _price[idx-1]<_price[idx]
                elif (val==1):
                    assert _price[idx-1]==_price[idx]
                else:
                    assert _price[idx-1]>_price[idx]
    
    assert isclose(total_prob, 1.0)