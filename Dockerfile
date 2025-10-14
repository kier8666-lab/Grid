FROM python:3.12-slim
WORKDIR /app
RUN pip install fastapi uvicorn
COPY mock_agent.py .
EXPOSE 8081
CMD ["uvicorn", "mock_agent:app", "--host", "0.0.0.0", "--port", "8081"]
