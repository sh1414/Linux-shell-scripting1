from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

requests = Counter('requests_total', 'Total Requests')

@app.route("/")
def home():
    requests.inc()
    return "Hello from CI/CD monitored app!"

@app.route("/metrics")
def metrics():
    return generate_latest()

app.run(host="0.0.0.0", port=5000)
