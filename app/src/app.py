from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({"status": "ok", "message": "DevOps demo app is running"}), 200

@app.route("/metrics")
def metrics():
    return "demo_requests_total 1\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
