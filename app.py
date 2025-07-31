from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)
# app.py dosyasını üzerine yaz:
cat > app.py << 'EOF'
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(f"🔥 n8n Webhook Alındı: {json.dumps(data, indent=2)}")
    return jsonify({"status": "success", "message": "Webhook received!"})

@app.route("/test-webhook", methods=["POST"])
def test_webhook():
    test_data = {
        "message": "Test mesajı n8n'den",
        "timestamp": "2024-07-31T18:45:00Z",
        "data": {"test": True, "user_id": 12345}
    }
    return jsonify(test_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
