import React, { useState } from 'react';
import axios from 'axios';
import { Form, Button, ListGroup } from 'react-bootstrap';

const QuestionList = ({ filteredQuestions, fetchQuestions }) => {
    const [editModeQuestions, setEditModeQuestions] = useState(new Set()); // State variable for questions in edit mode

    const deleteQuestion = async (questionId) => {
        try {
            await axios.delete(`https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions/${questionId}`);
            fetchQuestions(); // Fetch updated questions after deleting one
        } catch (error) {
            console.error('Error deleting question:', error);
        }
    };

    const updateQuestion = async (updatedQuestion) => {
        try {
            await axios.put(`https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions/${updatedQuestion.id}`, updatedQuestion);
            fetchQuestions(); // Fetch updated questions after updating one
        } catch (error) {
            console.error('Error updating question:', error);
        }
    };

    const handleChoiceChange = (e, index, question) => {
        const choices = [...question.choices];
        choices[index] = e.target.value;
        updateQuestion({ ...question, choices });
    };

    const addChoiceInput = async (question) => {
        const choices = [...question.choices, '']; // Add an empty choice
        try {
            await axios.put(`https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions/${question.id}`, { ...question, choices });
            fetchQuestions(); // Fetch updated questions after adding choice
        } catch (error) {
            console.error('Error adding choice:', error);
        }
    };

    const removeChoiceInput = async (index, question) => {
        const choices = [...question.choices.slice(0, index), ...question.choices.slice(index + 1)];
        try {
            await axios.put(`https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions/${question.id}`, { ...question, choices });
            fetchQuestions(); // Fetch updated questions after removing choice
        } catch (error) {
            console.error('Error removing choice:', error);
        }
    };

    const handleUpdateQuestion = async (question) => {
        try {
            await axios.put(`https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions/${question.id}`, question);
            fetchQuestions(); // Fetch updated questions after updating
            setEditModeQuestions((prevEditModeQuestions) => {
                const updatedEditModeQuestions = new Set(prevEditModeQuestions);
                updatedEditModeQuestions.delete(question.id);
                return updatedEditModeQuestions;
            });
        } catch (error) {
            console.error('Error updating question:', error);
        }
    };

    const toggleEditMode = (questionId) => {
        setEditModeQuestions((prevEditModeQuestions) => {
            const updatedEditModeQuestions = new Set(prevEditModeQuestions);
            if (updatedEditModeQuestions.has(questionId)) {
                updatedEditModeQuestions.delete(questionId);
            } else {
                updatedEditModeQuestions.add(questionId);
            }
            return updatedEditModeQuestions;
        });
    };

    return (
        <div className="question-list-container">
            <h2>Questions</h2>
            <ListGroup className="question-list">
                {filteredQuestions.map((question) => (
                    <ListGroup.Item key={question.id} className="question-item">
                        <Form>
                            <Form.Group controlId={`question-${question.id}`}>
                                <Form.Label><strong>Question:</strong></Form.Label>
                                <Form.Control
                                    type="text"
                                    value={question.question}
                                    onChange={(e) => updateQuestion({ ...question, question: e.target.value })}
                                    readOnly={!editModeQuestions.has(question.id)}
                                />
                            </Form.Group>

                            <Form.Group controlId={`choices-${question.id}`}>
                                <Form.Label><strong>Choices:</strong></Form.Label>
                                {question.choices.map((choice, index) => (
                                    <div key={index} className="choice-container d-flex align-items-center">
                                        <Form.Control
                                            type="text"
                                            value={choice}
                                            onChange={(e) => handleChoiceChange(e, index, question)}
                                            readOnly={!editModeQuestions.has(question.id)}
                                        />
                                        {editModeQuestions.has(question.id) && (
                                            <Button variant="danger" onClick={() => removeChoiceInput(index, question)}>Remove</Button>
                                        )}
                                    </div>
                                ))}
                                {editModeQuestions.has(question.id) && (
                                    <Button variant="success" onClick={() => addChoiceInput(question)}>Add Choice</Button>
                                )}
                            </Form.Group>

                            {editModeQuestions.has(question.id) && (
                                <Form.Group controlId={`correct-answer-${question.id}`}>
                                    <Form.Label><strong>Correct Answer:</strong></Form.Label>
                                    <Form.Control
                                        type="text"
                                        value={question.correct_answer}
                                        onChange={(e) => updateQuestion({ ...question, correct_answer: e.target.value })}
                                    />
                                </Form.Group>
                            )}

                            {editModeQuestions.has(question.id) && (
                                <>
                                    <Button variant="danger" onClick={() => deleteQuestion(question.id)}>Delete</Button>
                                    <Button variant="primary" onClick={() => handleUpdateQuestion(question)}>Update</Button>
                                </>
                            )}

                            {!editModeQuestions.has(question.id) && (
                                <Button variant="info" onClick={() => toggleEditMode(question.id)}>
                                    {editModeQuestions.has(question.id) ? 'Finish Editing' : 'Edit'}
                                </Button>
                            )}
                        </Form>
                    </ListGroup.Item>
                ))}
            </ListGroup>
        </div>
    );
};

export default QuestionList;
