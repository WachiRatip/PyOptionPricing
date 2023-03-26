import time

from option_pricing.bimodel import BinomialModel
from option_pricing.trimodel import TrinomialModel
from option_pricing.mcmodel import BlackScholesModel
from option_pricing import monte_carlo, options

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Took {(end_time - start_time)} seconds\n")
        return result
    return wrapper

@time_it
def display_binomial_model():
    print("Start Binomial Pricing Model")
    S0 = 100
    u = 0.1
    d = -0.1
    r = 0.0
    N = 20
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


@time_it
def display_multiprocessing_binomial_model():
    print("Start Binomial Pricing Model (Multiprocessing)")
    S0 = 100
    u = 0.1
    d = -0.1
    r = 0.0
    N = 20
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
    print("--Call Option price: ", option.multi_get_option_price())

    option = options.EuropeanPutOption(model = model, strike = K)
    print("--Put Option price : ", option.multi_get_option_price())

    print("-Asian Options:")
    option = options.AsianCallOption(model = model, strike = K)
    print("--Call Option price: ", option.multi_get_option_price())

    option = options.AsianPutOption(model = model, strike = K)
    print("--Put Option price : ", option.multi_get_option_price())


@time_it
def display_trinomial_model():
    print("Start Trinomial Pricing Model")
    S0 = 100.0
    sigma = 0.1
    T = 1.0
    r = 0.0
    N = 10
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


@time_it
def display_monte_carlo_model():
    print("Start Monte Carlo Pricing Model")
    S0 = 100.0
    sigma = 0.1
    T = 1.0
    r = 0.0
    step = 10
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


if __name__=="__main__":
    display_binomial_model()
    display_multiprocessing_binomial_model()
    display_trinomial_model()
    display_monte_carlo_model()