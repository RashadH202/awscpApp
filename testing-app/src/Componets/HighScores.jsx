import React, { useState, useEffect } from 'react';
import axios from 'axios';

const HighScore = () => {
    // State to store high scores
    const [highScores, setHighScores] = useState([]);

    // useEffect hook to fetch high scores when the component mounts
    useEffect(() => {
        fetchHighScores();
    }, []);

    // Function to fetch high scores from the API
    const fetchHighScores = async () => {
        try {
            // Fetch high scores data from the API
            const response = await axios.get('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/highscores');
            // Set the fetched high scores in the state
            setHighScores(response.data);
        } catch (error) {
            console.error('Error fetching high scores:', error);
        }
    };

    return (
        <div className="high-scores-container"> {/* Apply a class for the container */}
            <h2>High Scores</h2>
            <ul>
                {/* Map through the highScores array and render each high score */}
                {highScores.map((score, index) => (
                    <li key={index} className="high-score"> {/* Apply a class for each high score item */}
                        <p>
                            {/* Render high score details */}
                            <span className="name">{score.name}</span> -
                            <span className="score">{score.score}</span> - 
                            <span className="time">{score.numberOfQuestions}</span> - 
                            <span className="number">{score.timeFinished}</span>
                        </p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default HighScore;
