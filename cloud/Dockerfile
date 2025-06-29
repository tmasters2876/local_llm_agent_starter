# Use a slim Python image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy files
COPY . .

# Install deps
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Default command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
