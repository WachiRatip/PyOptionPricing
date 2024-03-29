# PyOptionPricing
A Pure Python implementation for calculating Call/Put option prices

# For testing the implementation
You can use either virtual environments or containers for testing this module.

1. Use virtual environments
    
    1.1 create a virtual environment.
    ```
    python -m venv .venv
    ```
    1.2 activate the virtual environment.
    ```
    .\.venv\Scripts\activate
    ```
    1.3 install dependencies for testing modules.
    ```
    pip install -r dev.requirements.txt
    ```
    1.4 run the tests.
    ```
    python -m pytest ./tests/
    ```
2. Use Docker containers

    2.1 install Docker in your local machine

    2.2 build the Docker image
    ```
    docker build -t option_pricing-test -f Dockerfile.test .
    ```
    2.3 run the tests 
    ```
    docker run --rm option_pricing-test
    ```

# TO-DO
- [ ] Add input dividend yield
- [x] Add Trinomial pricing models
- [x] Add test cases for Trinomial modeling
- [x] Add test cases for Trinomial European call/put options
- [x] Add test cases for Trinomial Asian call/put options
- [ ] Add geometric averaging to Asian options
    - [x] Add classes for Geometric Asian options
    - [ ] Rename the class of Asian options to arithmetic Asian options
    - [x] Add test cases for Binomial/Trinomial/Monte-Carlo Geometric Asian options
- [ ] Add American call/put options
- [ ] Add test cases for Binomial/Trinomial American call/put option
- [ ] Add fixed price Asian call/put options
- [ ] Add test cases for Binomial/Trinomial fixed price Asian call/put option
- [ ] Add Lookback call/put options
- [ ] Add test cases for Binomial/Trinomial Lookback call/put option
- [ ] Add Knockout call/put options
- [ ] Add test cases for Binomial/Trinomial Knockout call/put option
- [ ] Add classic Parisian call/put options
- [ ] Add test cases for Binomial/Trinomial classic Parisian call/put option

Add Finite difference methods for option pricing
- [ ] Add Explicit Finite difference methods
- [ ] Add Implicit Finite difference methods
- [ ] Add Crank–Nicolson Finite difference methods
- [ ] Add test cases for Finite difference methods

Add Monte Carlo methods for option pricing
- [x] Add a Monte Carlo option model
- [x] Add test cases for the Monte Carlo option model 
- [ ] Add Greek parameters
    - [ ] delta
    - [ ] gemma
    - [ ] vega
    - [ ] theta
    - [ ] rho
- [ ] Add the Variance reduction method to compute Monte Carlo pricing
- [x] Add benchmarking

# Speed test results
Users can run the following steps to conduct the speed testing on their machines.
```
cd benchmarking
python .\benchmark.py --debug
```
The following benchmarking was performed using Docker.
```
cd benchmarking
python .\docker_benchmark.py
```
When calculating option prices via Monte Carlo simulation with step=252 and n_sim=1_000, the results (averaged 5 times) for the last three major Python versions and the latest PyPy versions:
```
Python 3.9 took 4.9028668880462645 seconds per run.

Python 3.10 took 3.777042102813721 seconds per run.

Python 3.11 took 2.761995315551758 seconds per run.

PyPy 3.9 took 0.6229269981384278 seconds per run.
```