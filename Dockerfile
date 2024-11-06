# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install virtualenv
RUN pip install --no-cache-dir virtualenv

# Create and activate virtual environment
RUN virtualenv venv
ENV PATH="/app/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt /app/
RUN /app/venv/bin/pip install -r requirements.txt

# Copy the project files
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]