import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Modal, Button } from 'react-bootstrap';

const TestGenerator = () => {
    // State variables
    const [questions, setQuestions] = useState([]);
    const [selectedQuestions, setSelectedQuestions] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [userAnswers, setUserAnswers] = useState({}); // Store user's answers

    // Fetch questions from the backend when the component mounts
    useEffect(() => {
        fetchQuestions();
    }, []);

    // Fetch questions from the backend
    const fetchQuestions = async () => {
        try {
          const response = await axios.get('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions');
          setQuestions(response.data);
        } catch (error) {
          console.error('Error fetching questions:', error);
        }
    };

    // Generate test with a fixed number of questions (65)
    const generateTest = () => {
        const selected = [];

        // Select random questions to meet the fixed number (65)
        const shuffledQuestions = questions.sort(() => 0.5 - Math.random());
        for (let i = 0; i < 40 && i < shuffledQuestions.length; i++) {
            selected.push(shuffledQuestions[i]);
        }

        setSelectedQuestions(selected);
        setShowModal(true);
    };

    // Close the modal and reset user's answers
    const handleCloseModal = () => {
        setShowModal(false);
        setUserAnswers({});
    };

    // Update user's answers when they select an option
    const handleUserAnswer = (questionId, selectedAnswer) => {
        setUserAnswers(prevAnswers => ({
            ...prevAnswers,
            [questionId]: selectedAnswer
        }));
        console.log(`User answered question ${questionId}: ${selectedAnswer}`);
    };

    // Check if the user's answer is correct
    const isAnswerCorrect = (questionId, selectedAnswer) => {
        const question = selectedQuestions.find(q => q.id === questionId);
        return question.correct_answer.includes(selectedAnswer);
    };

    // Render the choices as 'A', 'B', 'C', 'D'
    const choicesLabels = ['A', 'B', 'C', 'D'];

    return (
        <div>
            40 Queestions: <Button onClick={generateTest}>Practice Test</Button>
            {/* Modal component */}
            <Modal show={showModal} onHide={handleCloseModal}>
                {/* Modal Header */}
                <Modal.Header closeButton>
                    <Modal.Title>Practice Test</Modal.Title>
                </Modal.Header>
                {/* Modal Body */}
                <Modal.Body>
                    {selectedQuestions.map(question => (
                        <div key={question.id} className="question-container">
                            {/* Question prompt */}
                            <p className="question">{question.question}</p>
                            {/* Render answer choices */}
                            {question.choices.map((choice, index) => (
                                <div key={choice} className="choice">
                                    <label>
                                        {/* Render choice label (A, B, C, D) */}
                                        <span className="choice-label">{choicesLabels[index]}. </span>
                                        {/* Radio button for selecting the choice */}
                                        <input
                                            type="radio"
                                            name={`question_${question.id}`}
                                            value={choice}
                                            onChange={() => handleUserAnswer(question.id, choice)}
                                        />
                                        {/* Display choice */}
                                        {choice}
                                    </label>
                                </div>
                            ))}
                            {/* Display whether the answer is correct or wrong */}
                            {userAnswers[question.id] && (
                                <p className="answer-feedback">
                                    {isAnswerCorrect(question.id, userAnswers[question.id])
                                        ? 'Your answer is correct!'
                                        : `Your answer is wrong. The correct answer is: ${question.correct_answer}`}
                                </p>
                            )}
                        </div>
                    ))}
                </Modal.Body>
                {/* Modal Footer */}
                <Modal.Footer>
                    {/* Close button */}
                    <Button variant="secondary" onClick={handleCloseModal}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>
    );
};

export default TestGenerator;
