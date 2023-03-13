
import math
import itertools
from option_pricing.bsmodel import BlackScholesModel


class Option():
    def __init__(self, model: BlackScholesModel) -> None:
        self.model = model

    def get_option_price(self, n_sim: int) -> tuple[float,float]:
        assert (n_sim > 1 and isinstance(n_sim, int))
        _payoff = 0.0
        _squared_payoff = 0.0
        for _ in itertools.repeat(None, n_sim):
            self.model.get_sample_path()
            _payoff += self.payoff(self.model.prices)
            _squared_payoff += self.payoff(self.model.prices)**2
            self.model.clear_path()
        
        price_approx = math.exp(-self.model.rate*self.model.m_time)*_payoff/n_sim
        price_err = math.exp(-self.model.rate*self.model.m_time)/math.sqrt(n_sim-1)*\
            math.sqrt(_squared_payoff/n_sim - (_payoff/n_sim)**2)
        return (price_approx, price_err)

    def payoff(self, prices: list[float]) -> float:
        pass

class EuropeanOption(Option):
    def __init__(self, model: BlackScholesModel, strike: float):
        super().__init__(model)
        # get user's input
        assert (strike > 0)
        self.strike = strike

class EuropeanCallOption(EuropeanOption):
    def payoff(self, prices: list[float]) -> float:
        _price = prices[-1] # the final stock price in the path
        return max(0, _price - self.strike)

class EuropeanPutOption(EuropeanOption):
    def payoff(self, prices: list[float]) -> float:
        _price = prices[-1] # the final stock price in the path
        return max(0, self.strike - _price)

class AsianOption(Option):
    def __init__(self, model: BlackScholesModel, strike: float):
        super().__init__(model)
        # get user's input
        assert (strike > 0)
        self.strike = strike
    
    def arithmetic_average(self, prices: list[float]) -> float:
        _average = 0
        for price in prices:
            _average += price
        
        return _average/len(prices)

class AsianCallOption(AsianOption):
    def payoff(self, prices: list[float]) -> float:
        _average = self.arithmetic_average(prices)
        return max(0.0, _average - self.strike)

class AsianPutOption(AsianOption):
    def payoff(self, prices: list[float]) -> float:
        _average = self.arithmetic_average(prices)
        return max(0.0, self.strike - _average)