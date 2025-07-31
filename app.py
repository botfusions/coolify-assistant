from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ask", methods=["POST"])
def ask():
    msg = request.json.get("message", "")
    return jsonify({"reply": f"👋 Mesajınız alındı: {msg}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)
