from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>🤖 AI Asistanı Çalışıyor!</h1>"

@app.route("/ask", methods=["POST"])
def ask():
    msg = request.json.get("message", "")
    return jsonify({"reply": f"👋 Mesajınız alındı: {msg}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)
