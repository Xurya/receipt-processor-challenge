# Use python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /usr/src/receipt-processor

# Dependency setup
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy files after to optimize rebuild on file changes other than dependencies
COPY . .

# Expose port 
EXPOSE 5000

# Run service
CMD ["python", "app.py"]
