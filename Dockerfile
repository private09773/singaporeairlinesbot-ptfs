FROM python:3.11-slim

WORKDIR /app
COPY . .

# Run requirements.sh with detection logic
RUN chmod +x requirements.sh && ./requirements.sh

CMD ["python", "main.py"]