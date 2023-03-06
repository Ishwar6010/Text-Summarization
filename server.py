from flask import Flask, jsonify
from transformers import pipeline

app = Flask(__name__)


@app.route('/summary/<string:text>', methods=["GET"])
def summary(text):
    summary_text = summarizer(text)[0]['summary_text']
    return jsonify({'SummarizedText': summary_text, 'Code': 200})


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
if __name__ == "__main__":
    app.run(debug=True, port=5005)
