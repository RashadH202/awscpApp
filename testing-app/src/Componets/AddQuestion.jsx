import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Form, Button } from 'react-bootstrap';

const AddQuestion = ({ fetchQuestions }) => {
    // Define state to manage the new question's data
    const [newQuestion, setNewQuestion] = useState({
        id: '',
        question: '',
        choices: [''],
        correct_answer: ''
    });

    // useEffect hook to fetch the highest ID present in the database when the component mounts
    useEffect(() => {
        const fetchHighestId = async () => {
            try {
                // Fetch questions data from the API
                const response = await axios.get('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions/');
                const questions = response.data;
                // Find the highest ID among fetched questions
                const highestId = questions.reduce((maxId, question) => Math.max(maxId, parseInt(question.id)), 0);
                // Set the ID for the new question
                setNewQuestion(prevState => ({ ...prevState, id: String(highestId + 1) }));
            } catch (error) {
                console.error('Error fetching highest ID:', error);
            }
        };
        fetchHighestId();
    }, []);

    // Function to handle input change for choices
    const handleInputChange = (e, index) => {
        const { value } = e.target;
        // Copy the current choices array
        const choices = [...newQuestion.choices];
        // Update the value of the choice at the specified index
        choices[index] = value;
        // Update the state with the new choices array
        setNewQuestion({ ...newQuestion, choices });
    };

    // Function to add a new choice input field
    const addChoiceInput = () => {
        // Add an empty choice to the choices array
        setNewQuestion({ ...newQuestion, choices: [...newQuestion.choices, ''] });
    };

    // Function to remove a choice input field
    const removeChoiceInput = (index) => {
        // Copy the current choices array
        const choices = [...newQuestion.choices];
        // Remove the choice at the specified index
        choices.splice(index, 1);
        // Update the state with the new choices array
        setNewQuestion({ ...newQuestion, choices });
    };

    // Function to add a new question
    const addQuestion = async () => {
        try {
            // Log the newQuestion object to the console
            console.log('New Question:', newQuestion);

            // Send a POST request to add the new question to the database
            await axios.post('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions/', newQuestion);

            // Clear the input fields and fetch the updated list of questions
            setNewQuestion({ id: '', question: '', choices: [''], correct_answer: '' });
            fetchQuestions();
        } catch (error) {
            console.error('Error adding question:', error);
        }
    };

    return (
        <Container>
            <h2>Add New Question</h2>
            <Form>
                {/* Input field for the question */}
                <Form.Group controlId="question">
                    <Form.Label>Question</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Question"
                        value={newQuestion.question}
                        onChange={(e) => setNewQuestion({ ...newQuestion, question: e.target.value })}
                    />
                </Form.Group>
                {/* Input fields for choices */}
                {newQuestion.choices.map((choice, index) => (
                    <Form.Group key={index} controlId={`choice-${index}`}>
                        <Form.Label>Choice {index + 1}</Form.Label>
                        <Form.Control
                            type="text"
                            placeholder={`Choice ${index + 1}`}
                            value={choice}
                            onChange={(e) => handleInputChange(e, index)}
                        />
                        {/* Button to remove the choice */}
                        <Button variant="danger" onClick={() => removeChoiceInput(index)}>Remove</Button>
                    </Form.Group>
                ))}
                {/* Button to add a new choice input field */}
                <Button variant="secondary" onClick={addChoiceInput}>Add Choice</Button>
                {/* Input field for the correct answer */}
                <Form.Group controlId="correctAnswer">
                    <Form.Label>Correct Answer</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Correct Answer"
                        value={newQuestion.correct_answer}
                        onChange={(e) => setNewQuestion({ ...newQuestion, correct_answer: e.target.value })}
                    />
                </Form.Group>
                {/* Button to add the question */}
                <Button variant="primary" onClick={addQuestion}>Add Question</Button>
            </Form>
        </Container>
    );
};

export default AddQuestion;
