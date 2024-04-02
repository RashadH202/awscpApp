import React, { useState, useEffect } from 'react';
import axios from 'axios';


const HighScore = () => {
    // State to store high scores
    const [highScores, setHighScores] = useState([]);

    useEffect(() => {
        fetchHighScores();
    }, []);

    const fetchHighScores = async () => {
        try {
            const response = await axios.get('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/highscores');
            setHighScores(response.data);
        } catch (error) {
            console.error('Error fetching high scores:', error);
        }
    };


    return (
        <div className="high-scores-container"> {/* Apply a class for the container */}
            <h2>High Scores</h2>
            <ul>
                {highScores.map((score, index) => (
                    <li key={index} className="high-score"> {/* Apply a class for each high score item */}
                        <p>
                            <span className="score">{score.score}</span> - 
                            <span className="time">{score.timetofinish}</span> - 
                            <span className="number">{score.numberofquestions}</span>
                            <span className="name">{score.name}</span>
                        </p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default HighScore;
