# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy Pipenv files first to install deps early
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy rest of the app (code, static files, templates)
COPY . .

# Install system dependencies 
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set NLTK data location and download necessary corpora
ENV NLTK_DATA=/usr/share/nltk_data
RUN pipenv run python -m nltk.downloader -d /usr/share/nltk_data wordnet omw-1.4

# Expose port for Flask app
EXPOSE 5001

# Run the Flask app
CMD ["pipenv", "run", "python", "app.py"]