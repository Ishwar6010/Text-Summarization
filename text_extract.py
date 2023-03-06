import json

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/text/', methods=["GET", "POST"])
def text():
    doc = request.files["file"]
    if doc.filename.lower().endswith(('.txt')):
        x = doc.read().decode("utf-8")
        url = "http://127.0.0.1:5005/update/" + x
        response = requests.get(url=url)
        passage = response.content.decode("utf-8").split(':')[1]
        print(passage)
        return passage
    else:
        return jsonify({'File Format': 'Not Supported', 'code': 400})


if __name__ == "__main__":
    app.run(debug=True, port=5006)
