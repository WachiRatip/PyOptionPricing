class BaseModel():
    def __init__(self, rate: float, n_step: int) -> None:
        self.rate = rate
        self.n_step = n_step
        self.path = [0]*n_step
        self.total_path: int = 2**n_step
        self.prices = [0.0]*n_step

    def get_path(self, x: int) -> None:
        pass

    # get a stock price at i-th step of path x 
    def get_price(self, x: int, i: int) -> float:
        pass
    
    def get_path_prices(self) -> None:
        pass

    def get_path_prob(self) -> float:
        pass

    def get_risk_neutral_prob(self) -> tuple[float]:
        pass

    def clear_path(self) -> None:
        self.path = [0]*self.n_step
        self.prices = [0.0]*self.n_step