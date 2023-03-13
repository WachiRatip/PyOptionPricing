from math import exp, log
from option_pricing.basemodel import BaseModel


class Option():
    def __init__(self, model: BaseModel) -> None:
        self.model = model

    # return the discounted price of expected payoff 
    def get_option_price(self) -> float:
        _option = 0
        for x in range(self.model.path_based_number**self.model.n_step):
            self.model.get_path(x)
            self.model.get_path_prices()
            _prob = self.model.get_path_prob()
            _payoff = self.payoff(self.model.prices)
            _option += _prob*_payoff

        _option = _option/((1+self.model.rate)**self.model.n_step)
        return _option
    
    def payoff(self, prices: list[float]) -> float:
        pass

class EuropeanOption(Option):
    def __init__(self, model: BaseModel, strike: float):
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
    def __init__(self, model: BaseModel, strike: float):
        super().__init__(model)
        # get user's input
        assert (strike > 0)
        self.strike = strike
    
    def arithmetic_average(self, prices: list[float]) -> float:
        _average = 0.0
        for price in prices:
            _average += price
        
        return _average/len(prices)
    
    def geometric_average(self, prices: list[float]) -> float:
        _average = 1.0
        for price in prices:
            _average *= price
        
        return exp(log(_average)/len(prices))

class AsianCallOption(AsianOption):
    def payoff(self, prices: list[float]) -> float:
        # the arithmetic average stock price in the path
        _price = self.arithmetic_average(prices)
        return max(0, _price - self.strike)

class AsianPutOption(AsianOption):
    def payoff(self, prices: list[float]) -> float:
        # the arithmetic average stock price in the path
        _price = self.arithmetic_average(prices)
        return max(0, self.strike - _price)

class GeometricAsianCallOption(AsianOption):
    def payoff(self, prices: list[float]) -> float:
        # the geometric average stock price in the path
        _price = self.geometric_average(prices)
        return max(0, _price - self.strike)

class GeometricAsianPutOption(AsianOption):
    def payoff(self, prices: list[float]) -> float:
        # the geometric average stock price in the path
        _price = self.geometric_average(prices)
        return max(0, self.strike - _price)