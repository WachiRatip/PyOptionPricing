import os
import sys
import time
import argparse

# Get the path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from option_pricing.mcmodel import BlackScholesModel
from option_pricing import monte_carlo


def benckmark_monte_carlo_model(n_steps=252, n_sims=1_000, n_repeats=5, debug=True):
    start_time = time.time()
    S0 = 100.0
    sigma = 0.3
    T = 1.0
    r = 0.05
    K = 130.0

    for _ in range(n_repeats):
        model = BlackScholesModel(S0, sigma, r, T, n_steps)
        option = monte_carlo.EuropeanCallOption(model, K)
        option.get_option_price(n_sims)
        del option
        option = monte_carlo.EuropeanPutOption(model, K)
        option.get_option_price(n_sims)
        del option
        option = monte_carlo.AsianCallOption(model, K)
        option.get_option_price(n_sims)
        del option
        option = monte_carlo.AsianPutOption(model, K)
        option.get_option_price(n_sims)
        del option
        option = monte_carlo.GeometricAsianCallOption(model, K)
        option.get_option_price(n_sims)
        del option
        option = monte_carlo.GeometricAsianPutOption(model, K)
        option.get_option_price(n_sims)
        del option
        del model

    if debug:
        print(f"Monte Carlo pricing models::")
        print(f"--Conducted tests with {n_sims} sample paths.")
        print(f"--Based on {n_repeats} times, it took {(time.time() - start_time)/n_repeats:.4f} seconds per run.")
    else:
        print(f"{(time.time() - start_time)/n_repeats}")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()
    benckmark_monte_carlo_model(debug=args.debug)