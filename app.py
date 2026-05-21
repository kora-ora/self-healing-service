from flask import Flask, jsonify
import os, datetime

app = Flask(__name__)
START_TIME = datetime.datetime.utcnow()

@app.route("/")
def home():
    return jsonify({
        "service": "self-healing-service",
        "status": "running"
    })

@app.route("/health")
def health():
    uptime = (datetime.datetime.utcnow() - START_TIME).seconds
    return jsonify({
        "status": "healthy",
        "uptime_seconds": uptime,
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
