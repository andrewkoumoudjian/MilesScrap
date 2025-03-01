FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# For Selenium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install chromedriver
RUN wget -q https://chromedriver.storage.googleapis.com/$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/bin \
    && rm chromedriver_linux64.zip \
    && chmod +x /usr/bin/chromedriver

# Copy application code
COPY . .

# Create cache directory
RUN mkdir -p cache

# Expose port for Flask
EXPOSE 8080

# Run with gunicorn
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app