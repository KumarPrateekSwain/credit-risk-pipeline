# Use official lightweight Python image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Set default command to run the API server or training script
CMD ["python", "-m", "src"]
