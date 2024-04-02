import React, { useState } from 'react';
import axios from 'axios';
import { Container, Form, Button } from 'react-bootstrap';

const AddQuestion = ({ fetchQuestions }) => {
    const [newQuestion, setNewQuestion] = useState({
        id: '',
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
    const addQuestionWithId = async () => {
      try {
          // Fetch the highest ID currently present in the database
          const response = await axios.get('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions');
          const questions = response.data;
          const highestId = questions.reduce((maxId, question) => Math.max(maxId, parseInt(question.id)), 0);
  
          // Increment the highest ID by 1 to generate a new ID for the new question
          const newId = highestId + 1;
  
          // Set the ID in the state
          setNewQuestion(prevState => ({ ...prevState, id: String(newId) }));
  
          // Create the new question object with the generated ID
          return { ...newQuestion, id: String(newId) };
      } catch (error) {
          console.error('Error generating new question with ID:', error);
          throw error;
      }
  };

    const addQuestion = async () => {
        try {
            // Generate the new question object with the id
            const questionWithId = await addQuestionWithId();

            // Log the question object with the id
            console.log('New question with id:', questionWithId);

            // Send the request to add the new question with the generated ID
            await axios.post('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions/', questionWithId);

            // Clear the input fields and fetch the updated list of questions
            setNewQuestion({ id: '', question: '', choices: [''], correct_answer: '' });
            fetchQuestions();
        } catch (error) {
            console.error('Error adding question:', error);
            console.log(newQuestion);
        }
    };

    return (
        <Container>
            <h2>Add New Question</h2>
            <Form>
                <Form.Group controlId="question">
                    <Form.Label>Question</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Question"
                        value={newQuestion.question}
                        onChange={(e) => setNewQuestion({ ...newQuestion, question: e.target.value })}
                    />
                </Form.Group>
                {newQuestion.choices.map((choice, index) => (
                    <Form.Group key={index} controlId={`choice-${index}`}>
                        <Form.Label>Choice {index + 1}</Form.Label>
                        <Form.Control
                            type="text"
                            placeholder={`Choice ${index + 1}`}
                            value={choice}
                            onChange={(e) => handleInputChange(e, index)}
                        />
                        <Button variant="danger" onClick={() => removeChoiceInput(index)}>Remove</Button>
                    </Form.Group>
                ))}
                <Button variant="secondary" onClick={addChoiceInput}>Add Choice</Button>
                <Form.Group controlId="correctAnswer">
                    <Form.Label>Correct Answer</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Correct Answer"
                        value={newQuestion.correct_answer}
                        onChange={(e) => setNewQuestion({ ...newQuestion, correct_answer: e.target.value })}
                    />
                </Form.Group>
                <Button variant="primary" onClick={addQuestion}>Add Question</Button>
            </Form>
        </Container>
    );
};

export default AddQuestion;
