FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies
COPY portfolio/nexus-labs/nexus-antikythera-recovery-v1/requirements.in .
RUN pip install --no-cache-dir -r requirements.in

# Copy application code
COPY portfolio/nexus-labs/nexus-antikythera-recovery-v1/app.py .
COPY portfolio/nexus-labs/nexus-antikythera-recovery-v1/templates/ ./templates/

# Expose port
EXPOSE 8731

# Run the app
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8731"]
