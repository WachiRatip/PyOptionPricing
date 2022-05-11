from option_pricing.bimodel import BinomialModel
from option_pricing.options import EuropeanCallOption, EuropeanPutOption, AsianCallOption, AsianPutOption

if __name__=="__main__":
    S0 = 100
    u = 0.1
    d = -0.1
    r = 0.0
    N = 3
    K = 130

    model = BinomialModel(
                spot = S0,
                up = u,
                down = d,
                rate = r,
                step = N
            )
    
    print("European Options:")
    option = EuropeanCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = EuropeanPutOption(model = model, strike = K)
    print("--Put Option price : ", option.get_option_price())

    print("Asian Options:")
    option = AsianCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = AsianPutOption(model = model, strike = K)
    print("--Put Option price : ", option.get_option_price())