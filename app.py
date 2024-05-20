# app.py

from flask import Flask, jsonify, request, render_template
from questions_db import questions_db
import random

app = Flask(__name__)

def get_question_by_difficulty(difficulty_level):
    questions = [q for q in questions_db if q["difficulty"] == difficulty_level]
    return random.choice(questions) if questions else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question', methods=['GET'])
def get_question():
    difficulty = request.args.get('difficulty')
    question = get_question_by_difficulty(difficulty)
    if question:
        options = question["options"]
        return jsonify({'text': question["question"], 'options': options})
    return jsonify({'error': 'No question found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
