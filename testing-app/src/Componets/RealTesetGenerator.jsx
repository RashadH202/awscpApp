import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Modal, Button } from 'react-bootstrap';

const RealTestGenerator = () => {
    const [questions, setQuestions] = useState([]);
    const [selectedQuestions, setSelectedQuestions] = useState([]);
    const [totalQuestions, setTotalQuestions] = useState(100);
    const [showModal, setShowModal] = useState(false);
    const [userAnswers, setUserAnswers] = useState({});
    const [timeLeft, setTimeLeft] = useState(4200);
    const [isTestSubmitted, setIsTestSubmitted] = useState(false);
    const [score, setScore] = useState(0);
    const [username, setUsername] = useState('');

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
            const response = await axios.get('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions');
            setQuestions(response.data);
        } catch (error) {
            console.error('Error fetching questions:', error);
        }
    };

    const generateTest = () => {
        const selected = [];
        const shuffledQuestions = questions.sort(() => 0.5 - Math.random());
        for (let i = 0; i < totalQuestions && i < shuffledQuestions.length; i++) {
            selected.push(shuffledQuestions[i]);
        }
        setSelectedQuestions(selected);
        setShowModal(true);
        setTimeLeft(4200);
        setIsTestSubmitted(false);
        setUserAnswers({});
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

    const handleSubmitTest = async () => {
        if (!username.trim()) {
            alert('Please enter your username.');
            return;
        }

        setIsTestSubmitted(true);
        const correctAnswers = selectedQuestions.filter(question => {
            // Check if user's answer is part of the correct answer
            return question.correct_answer.includes(userAnswers[question.id]);
        });
        const accuracyPercentage = (correctAnswers.length / totalQuestions) * 100;
        setScore(accuracyPercentage);

        try {
            const response = await axios.get('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/highscores');
            const highScores = response.data;
            const highestId = highScores.reduce((maxId, score) => Math.max(maxId, parseInt(score.id)), 0);
            const newId = highestId + 1;
            await axios.post('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/highscores', {
                id: newId.toString(),
                score: accuracyPercentage,
                timeFinished: new Date().toLocaleString(),
                numberOfQuestions: totalQuestions,
                name: username.trim() // Include the username in the submission
            });
            console.log("Test results submitted.");
        } catch (error) {
            console.error('Error sending test results:', error);
        }
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
            <Modal show={showModal} onHide={handleCloseModal}>
                {/* Modal Header */}
                <Modal.Header closeButton>
                    <Modal.Title>Timed Practice Test</Modal.Title>
                </Modal.Header>
                {/* Modal Body */}
                <Modal.Body>
                    <p>Time Left: {formatTime(timeLeft)}</p>
                    <input
                        type="text"
                        placeholder="Enter your username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        style={{ marginBottom: '10px' }}
                        disabled={isTestSubmitted}
                    />
                    <ul style={{ listStyleType: 'none', paddingLeft: 0 }}>
                        {/* Map through selected questions and render them */}
                        {selectedQuestions.map(question => (
                            <li key={question.id} className="question-container">
                                <p className="question">{question.question}</p>
                                <ul style={{ listStyleType: 'none', paddingLeft: 0 }}>
                                    {/* Map through choices of each question and render them */}
                                    {question.choices.map((choice, index) => (
                                        <li key={choice} className="choice">
                                            <label style={{ display: 'flex', alignItems: 'center' }}>
                                                {/* Render choice label */}
                                                <span className="choice-label">{String.fromCharCode(65 + index)}.</span>
                                                {/* Radio button for choice */}
                                                <input
                                                    type="radio"
                                                    name={`question_${question.id}`}
                                                    value={choice}
                                                    onChange={() => handleUserAnswer(question.id, choice)}
                                                    disabled={isTestSubmitted}
                                                />
                                                {/* Render choice */}
                                                {choice}
                                            </label>
                                        </li>
                                    ))}
                                </ul>
                                {/* Render correct answer if test is submitted */}
                                {isTestSubmitted && (
                                    <p className="answer-feedback">
                                        Correct Answer: {question.correct_answer}
                                    </p>
                                )}
                            </li>
                        ))}
                    </ul>
                    {/* Render submit button if test is not submitted */}
                    {!isTestSubmitted && (
                        <Button variant="primary" onClick={handleSubmitTest} className="submit-button">Submit Test</Button>
                    )}
                    {/* Render test result if test is submitted */}
                    {isTestSubmitted && (
                        <p className="answer-feedback">
                            {score >= 77 ? `Congratulations! You passed with a score of ${score}%` : `Sorry, you failed with a score of ${score}%`}
                        </p>
                    )}
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

export default RealTestGenerator;
