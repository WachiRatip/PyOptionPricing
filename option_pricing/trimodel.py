from math import exp, sqrt
from option_pricing.basemodel import BaseModel


class TrinomialModel(BaseModel):
    '''
    The constructor receives an initial stock price (spot), volatility (sigma), 
    interest rate (rate), time maturity of the option (m_time) and and number of time steps (n_step).
    '''
    def __init__(self, spot: float, sigma: float, rate: float, m_time: float, n_step: int) -> None:
        self.path_based_number = 3
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
        self.path = [0]*n_step
        self.prices = [0.0]*n_step

        # Set dt and dx according to given time maturity and number of time steps
        self.dt = self.m_time/self.n_step
        self.dx = self.sigma*sqrt(2*self.dt)

        # compute the risk-neutral probability and return the probabilties
        # for the stock price moving up, down and neutral respectively.
        self.prob_up, self.prob_down, self.prob_neutral = self.get_risk_neutral_prob()

    # generate path by the given number between 0 and 3^{n_step}-1
    def get_path(self, x: int) -> None:
        for idx in range(self.n_step):
            self.path[idx] = x%3
            x = int(x/3)

    # generate assosiated prices according to the corresponds path
    def get_path_prices(self) -> None:
        def get_stock(i: int):
            # return the stock price at node i-th.
            return self.spot*exp(i*self.dx)
        
        current_node = 0
        previous_node = 0

        for idx in range(self.n_step):
            current_node = self.path[idx] - 1
            if (idx == 0):
                self.prices[idx] = get_stock(current_node)
                previous_node = current_node
            else:
                self.prices[idx] = get_stock(previous_node + current_node)
                previous_node += current_node

    # compute the probability of an assosiated path
    def get_path_prob(self) -> float:
        num_up = 0
        num_down = 0
        num_neutral = 0

        for idx in range(self.n_step):
            if self.path[idx] == 0:
                num_down += 1
            elif self.path[idx] == 1:
                num_neutral += 1
            else:
                num_up += 1
        
        return (self.prob_up ** num_up) * (self.prob_down ** num_down) * (self.prob_neutral ** num_neutral)
    
    # compute risk neutual probabilties for moving up, down and neutral respectively.
    def get_risk_neutral_prob(self) -> tuple[float,float,float]:
        # the risk-neutral probability
        nu = self.rate-(self.sigma*self.sigma)*0.5
        prob_up = (((self.sigma*self.sigma*self.dt) + (nu*nu*self.dt*self.dt))/self.dx/self.dx + (nu*self.dt)/self.dx)*0.5
        prob_down = (((self.sigma*self.sigma*self.dt) + (nu*nu*self.dt*self.dt))/self.dx/self.dx - (nu*self.dt)/self.dx)*0.5
        prob_neutral = 1 - prob_up - prob_down
        return (prob_up, prob_down, prob_neutral)