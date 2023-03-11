class BinomialModel():
    def __init__(self, spot, up, down, rate, n_step):
        # valid inputs
        assert (spot > 0)
        assert (-1 < down < rate < up)
        assert (n_step >= 1 and isinstance(n_step, int))

        # set inputs
        self.spot = spot
        self.up = up
        self.down = down
        self.rate = rate
        self.n_step = n_step

        # set path's placeholders
        self.path = [0]*n_step
        self.prices = [0]*n_step

        # compute the risk-neutral probability and return the probabilties
        # for the stock price moving up and down respectively.
        self.prob_up, self.prob_down = self.get_risk_neutral_prob(up, down, rate)

    # generate path by given a path number x range from 0 to (2^{n_step} - 1)
    def get_path(self, x):
        for idx in range(self.n_step):
            self.path[idx] = x%2
            x = int(x/2)

    # generate assosiated prices according to the corresponds path
    def get_path_prices(self):
        _stock_price = self.spot
        for idx in range(self.n_step):
            if (self.path[idx] == 0):
                self.prices[idx] = _stock_price*(1+self.down)
            else:
                self.prices[idx] = _stock_price*(1+self.up)
            _stock_price = self.prices[idx]

    # compute the probability of an assosiated path
    def get_path_prob(self):
        num_up = 0
        num_down = 0
        for idx in range(self.n_step):
            if (self.path[idx] == 0):
                num_down += 1
            else:
                num_up += 1

        return (self.prob_up**num_up)*(self.prob_down**num_down)

    # compute probabilties for moving up and down respectively.
    def get_risk_neutral_prob(self, up, down, rate):
        # the risk-neutral probability
        q = (rate-down)/(up-down)
        return (q, 1-q)