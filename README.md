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
- [ ] Add benchmarking

# Speed test results
When calculating Asia call option prices via Monte Carlo simulation with step=50 and n_sim=100_000, the results (averaged 5 times) for the last five major Python versions and two PyPy versions:
```
The new Pypy 3.9 took 4.0327 seconds per run.

Python 3.7 took 28.192 seconds per run.(Pypy 3.9 is 599.1% faster)

Python 3.8 took 27.2714 seconds per run.(Pypy 3.9 is 576.3% faster)

Python 3.9 took 25.8714 seconds per run.(Pypy 3.9 is 541.5% faster)

Python 3.10 took 21.6086 seconds per run.(Pypy 3.9 is 435.8% faster)

Python 3.11 took 17.3501 seconds per run.(Pypy 3.9 is 330.2% faster)

Pypy 3.8 took 4.4112 seconds per run.(Pypy 3.9 is 9.4% faster)
```