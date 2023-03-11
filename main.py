from option_pricing.bimodel import BinomialModel
from option_pricing.trimodel import TrinomialModel
from option_pricing.options import EuropeanCallOption, EuropeanPutOption, AsianCallOption, AsianPutOption


def display_binomial_model():
    print("Start Binomial Pricing Model")
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
                n_step = N
            )
    
    print("-European Options:")
    option = EuropeanCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = EuropeanPutOption(model = model, strike = K)
    print("--Put Option price : ", option.get_option_price())

    print("-Asian Options:")
    option = AsianCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = AsianPutOption(model = model, strike = K)
    print("--Put Option price : ", option.get_option_price())
    print()

def display_trinomial_model():
    print("Start Trinomial Pricing Model")
    S0 = 100.0
    sigma = 0.1
    T = 1.0
    r = 0.0
    N = 3
    K = 130.0

    model = TrinomialModel(
                spot = S0,
                sigma= sigma,
                rate = r,
                m_time= T,
                n_step = N
    )

    print("-European Options:")
    option = EuropeanCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = EuropeanPutOption(model = model, strike = K)
    print("--Put Option price : ", option.get_option_price())

    print("-Asian Options:")
    option = AsianCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = AsianPutOption(model = model, strike = K)
    print("--Put Option price : ", option.get_option_price())
    print()

if __name__=="__main__":
    display_binomial_model()
    display_trinomial_model()
