import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
CORS(app)
BASE = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.get("/health")
def health():
    return jsonify(status="ok", project="Team J: Multilingual Voice Assistant", stack="flask")

@app.route("/api/transcribe", methods=["POST"])
def ep_0(**kwargs):
    # TODO: Audio file -> {text, language}
    return jsonify(error="Not implemented", todo="Audio file -> {text, language}"), 501

@app.route("/api/translate", methods=["POST"])
def ep_1(**kwargs):
    # TODO: Body: {text, target} -> {text}
    return jsonify(error="Not implemented", todo="Body: {text, target} -> {text}"), 501

@app.route("/api/speak", methods=["POST"])
def ep_2(**kwargs):
    # TODO: Body: {text, lang} -> audio
    return jsonify(error="Not implemented", todo="Body: {text, lang} -> audio"), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
