import random
import math


# Box–Muller method to generate a random variable with standard normal distribution N(0,1)
def get_rv_std_normal() -> float:
    U1 = random.uniform(0, 1)
    U2 = random.uniform(0, 1)
    return math.sqrt(-2.0 * math.log(U1)) * math.cos(2.0 * math.pi * U2)

class BlackScholesModel():
    def __init__(self, spot: float, sigma: float, rate: float, m_time: float, n_step: int) -> None:
        # valid inputs
        assert (spot > 0)
        assert (0.0 < sigma <= 1.0)
        assert (0.0 <= rate <= 1.0)
        assert (m_time > 0.0)
        assert (n_step >= 1 and isinstance(n_step, int))

        # set inputs
        self.spot = spot
        self.sigma = sigma
        self.rate = rate
        self.m_time = m_time
        self.n_step = n_step

        # set path's placeholders
        self.prices = [0.0]*n_step

    def clear_path(self) -> None:
        self.prices = [0.0]*self.n_step

    def get_sample_path(self) -> None:
        _price = self.spot
        for idx in range(self.n_step):
            self.prices[idx] = _price*math.exp(
                (self.rate-(self.sigma*self.sigma*0.5))*(self.m_time/self.n_step)+\
                    self.sigma*math.sqrt(self.m_time/self.n_step)*get_rv_std_normal()
            )
            _price = self.prices[idx]