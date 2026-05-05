FROM python:3.12-slim

# Create a non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Copy the application code and set ownership
COPY --chown=appuser:appgroup mock_agent.py .

# Switch to the non-root user
USER appuser

EXPOSE 8081

CMD ["uvicorn", "mock_agent:app", "--host", "0.0.0.0", "--port", "8081"]
