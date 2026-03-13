from flask import Flask, render_template, request, jsonify
from chatbot import get_dynamic_response
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    print(f"Received message: '{message}'")
    response = get_dynamic_response(message)
    print(f"Bot response: '{response}'")
    return jsonify({"reply": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)