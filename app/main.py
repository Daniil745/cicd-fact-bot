import os
import random
import time
from flask import Flask, jsonify

app = Flask(__name__)

BUG_MODE = os.getenv("BUG_MODE", "false")

facts = [
    "Средняя нагрузка за 5 минут: 0.5",
    "Свободно RAM: 2.3 ГБ",
    "Uptime сервера: 3 дня 4 часа",
    "Активных соединений: 12",
    "Дисковое I/O: 45 MB/s"
]

@app.route('/')
def home():
    """Главная страница - возвращает случайный факт"""
    return random.choice(facts)

@app.route('/health')
def health():
    """Healthcheck endpoint - для проверки что приложение живо"""
    
    if BUG_MODE == "true":
        print("[BUG] Медленный ответ /health, симулируем проблему...")
        time.sleep(15)
        return jsonify({"status": "slow", "message": "Service is degraded"}), 500
    
    return jsonify({"status": "ok", "service": "fact-bot"}), 200

@app.route('/metrics')
def metrics():
    """Простые метрики для демонстрации"""
    return jsonify({
        "bug_mode": BUG_MODE,
        "random_fact": random.choice(facts)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
