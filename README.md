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
    docker build -t option_pricing-test .
    ```
    2.3 run the tests 
    ```
    docker run --rm option_pricing-test
    ```

# TO-DO
- [x] Add Trinomial pricing model
- [x] Add test cases for Trinomial modeling
- [x] Add test cases for Trinomial European call/put option
- [x] Add test cases for Trinomial Asian call/put option
- [ ] Add American call/put option
- [ ] Add test cases for Trinomial American call/put option
- [ ] Add fixed price Asian call/put option
- [ ] Add test cases for Trinomial fixed price Asian call/put option
- [ ] Add Lookback call/put option
- [ ] Add test cases for Trinomial Lookback call/put option
- [ ] Add Knockout call/put option
- [ ] Add test cases for Trinomial Knockout call/put option
- [ ] Add classic Parisian call/put option
- [ ] Add test cases for Trinomial classic Parisian call/put option

Add Finite difference methods for option pricing
- [ ] Add Explicit Finite difference method
- [ ] Add Implicit Finite difference method
- [ ] Add Crank–Nicolson Finite difference method
- [ ] Add test cases for Finite difference methods

Add Monte Carlo methods for option pricing
- [ ] Add a Monte Carlo option model
- [ ] Add test cases for the Monte Carlo option model 
