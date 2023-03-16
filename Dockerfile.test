# Use the official Python image as the base image
FROM pypy:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the source code and test code into the container
COPY option_pricing/ /app/option_pricing/
COPY tests/ /app/tests/

# Install the development dependencies
COPY dev.requirements.txt /app/
RUN pip install -r dev.requirements.txt

# Set the environment variable for pytest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app/option_pricing

# Run the tests with pytest
CMD ["python", "-m", "pytest", "tests/"]
