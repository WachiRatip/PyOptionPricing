from option_pricing.bimodel import BinomialModel
from option_pricing.trimodel import TrinomialModel
from option_pricing.mcmodel import BlackScholesModel
from option_pricing import monte_carlo, options


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
    option = options.EuropeanCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = options.EuropeanPutOption(model = model, strike = K)
    print("--Put Option price : ", option.get_option_price())

    print("-Asian Options:")
    option = options.AsianCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = options.AsianPutOption(model = model, strike = K)
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
    option = options.EuropeanCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = options.EuropeanPutOption(model = model, strike = K)
    print("--Put Option price : ", option.get_option_price())

    print("-Asian Options:")
    option = options.AsianCallOption(model = model, strike = K)
    print("--Call Option price: ", option.get_option_price())

    option = options.AsianPutOption(model = model, strike = K)
    print("--Put Option price : ", option.get_option_price())
    print()

def display_monte_carlo_model():
    print("Start Monte Carlo Pricing Model")
    S0 = 100.0
    sigma = 0.1
    T = 1.0
    r = 0.0
    step = 3
    K = 130.0
    n_sim = 1000
    model = BlackScholesModel(S0, sigma, r, T, step)

    print("-European Options:")
    option = monte_carlo.EuropeanCallOption(model = model, strike = K)
    print("--Call Option price: %.4f with error %.4f" %option.get_option_price(n_sim))

    option = monte_carlo.EuropeanPutOption(model = model, strike = K)
    print("--Put Option price : %.4f with error %.4f" %option.get_option_price(n_sim))

    print("-Asian Options:")
    option = monte_carlo.AsianCallOption(model = model, strike = K)
    print("--Call Option price: %.4f with error %.4f" %option.get_option_price(n_sim))

    option = monte_carlo.AsianPutOption(model = model, strike = K)
    print("--Put Option price : %.4f with error %.4f" %option.get_option_price(n_sim))
    print()

if __name__=="__main__":
    display_binomial_model()
    display_trinomial_model()
    display_monte_carlo_model()