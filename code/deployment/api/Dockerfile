FROM python:3.11-slim

WORKDIR /api

COPY code/deployment/api/requirements.txt .
RUN pip install -r requirements.txt

COPY code/deployment/api/main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]