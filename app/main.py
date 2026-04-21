import os
import random
import time
from flask import Flask, jsonify

app = Flask(__name__)

BUG_MODE = os.getenv("BUG_MODE", "true")

facts = [
    "Average load over 5 minutes: 0.5",
    "Free RAM: 2.3 GB",
    "Server uptime: 3 days 4 hours",
    "Active connections: 12",
    "Disk I/O: 45 MB/s"
]

@app.route('/')
def home():
    return random.choice(facts)

@app.route('/health')
def health():
    if BUG_MODE == "true":
        time.sleep(15)
        return jsonify({"status": "slow", "message": "Service is degraded"}), 500
    
    return jsonify({"status": "ok", "service": "fact-bot"}), 200

@app.route('/metrics')
def metrics():
    return jsonify({
        "bug_mode": BUG_MODE,
        "random_fact": random.choice(facts)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
