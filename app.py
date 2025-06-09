from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Gauge

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Метрики Prometheus
visit_counter = Counter('homepage_visits_total', 'Total visits to homepage')
active_users = Gauge('active_users', 'Number of active users')

# Список текущих "подключённых" пользователей
current_users = []

@app.route('/')
def home():
    visit_counter.inc()
    active_users.set(len(current_users))  # Обновляем значение gauge
    return f"Привет! Сейчас онлайн: {len(current_users)}"

@app.route('/login')
def login():
    current_users.append('user')
    active_users.set(len(current_users))
    return f"Пользователь вошёл. Онлайн: {len(current_users)}"

@app.route('/logout')
def logout():
    if current_users:
        current_users.pop()
    active_users.set(len(current_users))
    return f"Пользователь вышел. Онлайн: {len(current_users)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

