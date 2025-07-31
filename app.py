from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(f"🔥 Webhook alındı: {data}")
    return jsonify({"status": "success", "message": "Webhook received!"})

@app.route("/test-webhook", methods=["POST"])
def test_webhook():
    return jsonify({
