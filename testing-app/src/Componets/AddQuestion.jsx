import React, { useState } from 'react';
import axios from 'axios';
import { Form, Button, Container, Row, Col } from 'react-bootstrap';


const AddQuestion = ({ fetchQuestions }) => {
  const [newQuestion, setNewQuestion] = useState({
    question: '',
    choices: [''],
    correct_answer: ''
  });

  const handleInputChange = (e, index) => {
    const { value } = e.target;
    const choices = [...newQuestion.choices];
    choices[index] = value;
    setNewQuestion({ ...newQuestion, choices });
  };

  const addChoiceInput = () => {
    setNewQuestion({ ...newQuestion, choices: [...newQuestion.choices, ''] });
  };

  const removeChoiceInput = (index) => {
    const choices = [...newQuestion.choices];
    choices.splice(index, 1);
    setNewQuestion({ ...newQuestion, choices });
  };

  const addQuestion = async () => {
    try {
      await axios.post('http://localhost:5000/questions', newQuestion);
      setNewQuestion({ question: '', choices: [''], correct_answer: '' });
      fetchQuestions();
    } catch (error) {
      console.error('Error adding question:', error);
    }
  };

  return (
    <Container className="add-question-container"> {/* Apply container styles */}
      <h2>Add New Question</h2>
      <Form>
        <Form.Group controlId="question" className="add-question-input"> {/* Apply input styles */}
          <Form.Label>Question</Form.Label>
          <Form.Control
            type="text"
            placeholder="Question"
            value={newQuestion.question}
            onChange={(e) => setNewQuestion({ ...newQuestion, question: e.target.value })}
          />
        </Form.Group>
        {newQuestion.choices.map((choice, index) => (
          <Row key={index} className="choice-item">
            <Col className="add-question-input"> {/* Apply input styles */}
              <Form.Group controlId={`choice-${index}`}>
                <Form.Label>Choice {index + 1}</Form.Label>
                <Form.Control
                  type="text"
                  placeholder={`Choice ${index + 1}`}
                  value={choice}
                  onChange={(e) => handleInputChange(e, index)}
                />
              </Form.Group>
            </Col>
            <Col className="choice-buttons"> {/* Apply button styles */}
              <Button variant="danger" onClick={() => removeChoiceInput(index)}>Remove</Button>
            </Col>
          </Row>
        ))}
        <Button variant="secondary" onClick={addChoiceInput} className="add-question-button"> {/* Apply button styles */}
          Add Choice
        </Button>
        <Form.Group controlId="correctAnswer" className="add-question-input"> {/* Apply input styles */}
          <Form.Label>Correct Answer</Form.Label>
          <Form.Control
            type="text"
            placeholder="Correct Answer"
            value={newQuestion.correct_answer}
            onChange={(e) => setNewQuestion({ ...newQuestion, correct_answer: e.target.value })}
          />
        </Form.Group>
        <Button variant="primary" onClick={addQuestion} className="add-question-button"> {/* Apply button styles */}
          Add Question
        </Button>
      </Form>
    </Container>
  );
};

export default AddQuestion;
