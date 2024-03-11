import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import { Container, Row, Col } from 'react-bootstrap';

import QuestionList from './Componets/QuestionList';
import NavBar from './Componets/NavBar';

function App() {
  // State variables
  const [questions, setQuestions] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');

  // Fetch questions from the backend when the component mounts
  useEffect(() => {
    fetchQuestions();
  }, []);

  // Fetch questions from the backend
  const fetchQuestions = async () => {
    try {
      const response = await axios.get('http://localhost:5000/questions');
      setQuestions(response.data.questions);
    } catch (error) {
      console.error('Error fetching questions:', error);
    }
  };

  // Delete a question by its ID
  const deleteQuestion = async (questionId) => {
    try {
      await axios.delete(`http://localhost:5000/questions/${questionId}`);
      fetchQuestions(); // Refetch questions after deletion
    } catch (error) {
      console.error('Error deleting question:', error);
    }
  };

  // Update a question with new data
  const updateQuestion = async (updatedQuestion) => {
    try {
      await axios.put(`http://localhost:5000/questions/${updatedQuestion.id}`, updatedQuestion);
      fetchQuestions(); // Refetch questions after update
    } catch (error) {
      console.error('Error updating question:', error);
    }
  };

  // Handle changes in the search input
  const handleSearchInputChange = (e) => {
    setSearchQuery(e.target.value);
  };

  // Filter questions based on the search query
  const filteredQuestions = questions.filter((question) =>
    question.question.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <Container fluid>
      {/* Navigation bar */}
      <Row>
        <Col>
          <NavBar
            fetchQuestions={fetchQuestions}
            handleSearchInputChange={handleSearchInputChange}
            searchQuery={searchQuery}
            questionCount={questions.length} // Pass the count of questions to the NavBar
          />
        </Col>
      </Row>
      {/* Question list */}
      <Row>
        <Col>
          <QuestionList
            filteredQuestions={filteredQuestions}
            fetchQuestions={fetchQuestions}
            deleteQuestion={deleteQuestion}
            updateQuestion={updateQuestion}
          />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
