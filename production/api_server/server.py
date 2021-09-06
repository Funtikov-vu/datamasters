from flask import Flask, jsonify, request
import os

import pandas as pd

from predict import predict

app = Flask(__name__)


@app.route('/user', methods=['GET'])
def get_cardio_user():
    return jsonify({'cardio': predict(request.json, 'user')})


@app.route('/main', methods=['GET'])
def get_cardio_main():
    return jsonify({'cardio': predict(request.json, 'main')})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
