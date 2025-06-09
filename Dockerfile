FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost:5000 || exit 1

CMD ["python", "app.py"]

