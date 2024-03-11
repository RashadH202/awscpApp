from flask import Flask, jsonify, request
from flask_cors import CORS
from question_data import question_bank  # Import question bank data
import uuid

app = Flask(__name__)
CORS(app)

# Define the high scores list
high_scores = []

# Helper function to find a question by ID
def find_question_by_id(question_id):
    for question in question_bank:
        if question['id'] == question_id:
            return question
    return None

# Route to add a new question to the question bank
@app.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    new_question_id = str(uuid.uuid4())  # Generate a unique UUID for the new question
    new_question = {
        'id': new_question_id,
        'question': data['question'],
        'choices': data['choices'],
        'correct_answer': data['correct_answer']
    }
    question_bank.append(new_question)
    return jsonify({'message': 'Question added successfully', 'question_id': new_question_id}), 201

# Route to get all questions from the question bank
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': question_bank}), 200

# Route to get a specific question by ID
@app.route('/questions/<question_id>', methods=['GET'])
def get_question(question_id):
    question = find_question_by_id(question_id)
    if question:
        return jsonify({'question': question}), 200
    else:
        return jsonify({'message': 'Question not found'}), 404

# Route to update a question by ID
@app.route('/questions/<question_id>', methods=['PUT'])
def update_question(question_id):
    question = find_question_by_id(question_id)
    if question:
        data = request.get_json()
        question['question'] = data['question']
        question['choices'] = data['choices']
        question['correct_answer'] = data['correct_answer']
        return jsonify({'message': 'Question updated successfully'}), 200
    else:
        return jsonify({'message': 'Question not found'}), 404

# Route to delete a question by ID
@app.route('/questions/<question_id>', methods=['DELETE'])
def delete_question(question_id):
    question = find_question_by_id(question_id)
    if question:
        question_bank.remove(question)
        return jsonify({'message': 'Question deleted successfully'}), 200
    else:
        return jsonify({'message': 'Question not found'}), 404

# Route to handle high scores
@app.route('/highscores', methods=['GET', 'POST'])
def handle_high_scores():
    if request.method == 'GET':
        return jsonify({'highScores': high_scores}), 200
    elif request.method == 'POST':
        data = request.get_json()
        high_scores.append({
            'score': data['score'],
            'timeFinished': data['timeFinished'],
            'numberOfQuestions': data['numberOfQuestions']
        })
        return jsonify({'message': 'High score added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
