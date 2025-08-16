FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual backend source code
COPY . .

# Default run command (overridden by docker-compose if needed)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
