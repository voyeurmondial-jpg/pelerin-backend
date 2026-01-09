from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenv("MONGO_URI"))
db = client.pelerinage

@app.route("/api/inscription", methods=["POST"])
def inscription():
    data = request.json
    db.pelerins.insert_one(data)
    return jsonify({"status": "ok"})

@app.route("/")
def health():
    return "API OK"

if __name__ == "__main__":
    app.run()
