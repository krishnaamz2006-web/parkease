from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/data")
def get_data():
 data = {
    "P1": 1,
    "P2": 0,
    "P3": random.choice([0,0,1]),  # less frequent change
    "P4": random.choice([0,1])}
 return jsonify(data)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)