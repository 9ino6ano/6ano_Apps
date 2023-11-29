# API script (api.py)
from flask import Flask, request, jsonify
from qa_model import get_answer

app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def answer_question():
    data = request.get_json()
    question = data['question']
    context = data.get('context', '')
    answer = get_answer(question, context)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
