# Dockerfile
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY ./src /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
