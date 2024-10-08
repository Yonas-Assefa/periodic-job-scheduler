# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # Prevents Python from writing .pyc files
ENV PYTHONUNBUFFERED 1  # Ensures output is sent straight to terminal

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libpq-dev gcc \
    && apt-get clean

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code
COPY . /app/
