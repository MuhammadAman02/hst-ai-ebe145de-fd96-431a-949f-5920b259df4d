FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create necessary directories if they don't exist
RUN mkdir -p static/data

# Set environment variables
ENV PORT=8000
ENV HOST=0.0.0.0

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "main.py"]