# Pull base image
FROM mcr.microsoft.com/playwright/python:v1.35.0-jammy

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.3.0

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /django
COPY poetry.lock pyproject.toml /django/

# Project initialization:
RUN poetry config virtualenvs.create false 
RUN poetry install --no-interaction --no-ansi

# Install Playwright deps
RUN playwright install --with-deps

# Creating folders, and files for the project:
COPY . /django/

# entrypoint for django server
ENTRYPOINT ["sh", "entrypoint.sh"]