from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Gauge
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Кастомная метрика: общее количество посещений
visit_counter = Counter('homepage_visits_total', 'Total visits to homepage')

# Кастомный Gauge: рандомное "число подключенных пользователей"
active_users = Gauge('active_users', 'Number of active users')

@app.route('/')
def home():
    visit_counter.inc()
    active_users.set(random.randint(1, 10))  # Пример, потом можно заменить реальными данными
    return "Привет! Метрики обновлены."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

