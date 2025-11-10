# Base image
FROM python:3.14

# Working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml poetry.lock* /app/

# Install poetry & dependencies
RUN pip install poetry && poetry install --no-root

# Copy the project code
COPY . /app

# Default command
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
