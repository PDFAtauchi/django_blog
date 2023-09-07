FROM cimg/python:3.8

# Set environment variables for Python and Poetry
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.3.0
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_HOME='/usr/local'

USER root

# Create and set the working directory
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the container
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root \
    && poetry --version \
    # Cleaning cache:
    && sudo apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && sudo apt-get clean -y && sudo rm -rf /var/lib/apt/lists/*

# Copy the Django project code into the container
COPY . /app/

# Expose the port that the Django development server will run on
EXPOSE 8000

# Start the Django development server
# entrypoint
ENTRYPOINT ["/app/entry.sh"]
