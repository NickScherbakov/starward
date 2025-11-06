FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ ./src/
COPY pyproject.toml .

# Install starward
RUN pip install --no-cache-dir -e .

# Create necessary directories
RUN mkdir -p /app/snapshots /app/logs

EXPOSE 4566

# Health check
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import httpx; httpx.get('http://localhost:4566/health', timeout=2)" || exit 1

# Default command starts the server
CMD ["starward", "up", "--host", "0.0.0.0", "--port", "4566"]
