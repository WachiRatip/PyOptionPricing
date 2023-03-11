class BaseModel():
    def __init__(self, rate: float, n_step: int) -> None:
        self.path_based_number: int = 2
        self.rate = rate
        self.n_step = n_step
        self.prices = [0.0]*n_step

    def get_path(self, x: int) -> None:
        pass

    def get_path_prices(self) -> None:
        pass

    def get_path_prob(self) -> float:
        pass

    def get_risk_neutral_prob(self) -> tuple[float]:
        pass