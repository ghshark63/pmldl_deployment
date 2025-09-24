FROM python:3.11-slim

WORKDIR /app

COPY code/deployment/app/requirements.txt .
RUN pip install -r requirements.txt

COPY code/deployment/app/main.py .

EXPOSE 8090

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8090", "--server.address=0.0.0.0"]