# PyOptionPricing
A Python implementation for calculating Call-Put option prices

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
