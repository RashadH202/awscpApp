import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Modal, Button } from 'react-bootstrap';

const RealTestGenerator = () => {
    const [questions, setQuestions] = useState([]);
    const [selectedQuestions, setSelectedQuestions] = useState([]);
    const [totalQuestions, setTotalQuestions] = useState(100); // Default total number of questions
    const [showModal, setShowModal] = useState(false);
    const [userAnswers, setUserAnswers] = useState({}); // Store user's answers
    const [timeLeft, setTimeLeft] = useState(4200); // Default time: 70 minutes in seconds
    const [isTestSubmitted, setIsTestSubmitted] = useState(false);
    const [score, setScore] = useState(0);

    useEffect(() => {
        fetchQuestions();
    }, []);

    useEffect(() => {
        if (showModal && timeLeft > 0) {
            const timer = setTimeout(() => {
                setTimeLeft(prevTime => prevTime - 1);
            }, 1000);

            return () => clearTimeout(timer);
        }
    }, [showModal, timeLeft]);

    const fetchQuestions = async () => {
        try {
            const response = await axios.get('http://localhost:5000/questions');
            setQuestions(response.data.questions);
        } catch (error) {
            console.error('Error fetching questions:', error);
        }
    };

    const generateTest = () => {
        const selected = [];

        // Select random questions to meet the total number specified by the user
        const shuffledQuestions = questions.sort(() => 0.5 - Math.random());
        for (let i = 0; i < totalQuestions && i < shuffledQuestions.length; i++) {
            selected.push(shuffledQuestions[i]);
        }

        setSelectedQuestions(selected);
        setShowModal(true);
        // Set timer to start automatically
        setTimeLeft(4200); // 70 minutes in seconds
        setIsTestSubmitted(false); // Reset test submission state
        setUserAnswers({}); // Reset user's answers
    };

    const handleCloseModal = () => {
        setShowModal(false);
    };

    const handleUserAnswer = (questionId, selectedAnswer) => {
        setUserAnswers(prevAnswers => ({
            ...prevAnswers,
            [questionId]: selectedAnswer
        }));
    };

    const handleSubmitTest = () => {
        setIsTestSubmitted(true);
        const correctAnswers = selectedQuestions.filter(question => userAnswers[question.id] === question.correct_answer);
        const accuracyPercentage = (correctAnswers.length / totalQuestions) * 100;
        setScore(accuracyPercentage);
    };

    const formatTime = (time) => {
        const minutes = Math.floor(time / 60);
        const seconds = time % 60;
        return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    };

    return (
        <div>
            <div>
                <span className='numberofquestions_nav'>Number of Questions:</span>
                <input type="number" value={totalQuestions} onChange={(e) => setTotalQuestions(e.target.value)} />
                <Button onClick={generateTest}>Timed Practice Test</Button>
            </div>
            {/* Modal component */}
            <Modal show={showModal} onHide={handleCloseModal}>
                <Modal.Header closeButton>
                    <Modal.Title>Timed Practice Test</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <p>Time Left: {formatTime(timeLeft)}</p>
                    <ul style={{ listStyleType: 'none', paddingLeft: 0 }}>
                        {selectedQuestions.map(question => (
                            <li key={question.id} className="question-container">
                                <p className="question">{question.question}</p>
                                <ul style={{ listStyleType: 'none', paddingLeft: 0 }}>
                                    {question.choices.map((choice, index) => (
                                        <li key={choice} className="choice">
                                            <label style={{ display: 'flex', alignItems: 'center' }}>
                                                <span className="choice-label">{String.fromCharCode(65 + index)}.</span>
                                                <input
                                                    type="radio"
                                                    name={`question_${question.id}`}
                                                    value={choice}
                                                    onChange={() => handleUserAnswer(question.id, choice)}
                                                    disabled={isTestSubmitted} // Disable inputs after test is submitted
                                                />
                                                {choice}
                                            </label>
                                        </li>
                                    ))}
                                </ul>
                                {isTestSubmitted && (
                                    <p className="answer-feedback">
                                        Correct Answer: {question.correct_answer}
                                    </p>
                                )}
                            </li>
                        ))}
                    </ul>
                    {!isTestSubmitted && (
                        <Button variant="primary" onClick={handleSubmitTest} className="submit-button">Submit Test</Button>
                    )}
                    {isTestSubmitted && (
                        <p className="answer-feedback">
                            {score >= 77 ? `Congratulations! You passed with a score of ${score}%` : `Sorry, you failed with a score of ${score}%`}
                        </p>
                    )}
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleCloseModal}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
        </div>
    );
};

export default RealTestGenerator;
