import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Row, Col } from 'react-bootstrap';
import './App.css'
import QuestionList from './Componets/QuestionList';
import HighScores from './Componets/HighScores';
import NavBar from './Componets/NavBar';

function App() {
  // State variables
  const [questions, setQuestions] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [showModal, setShowModal] = useState(false); // State for controlling modal visibility
  const [modalClosed, setModalClosed] = useState(false); // State for tracking modal closure

  // Fetch questions from the backend when the component mounts
  useEffect(() => {
    fetchQuestions();
  }, [modalClosed]); // Refetch questions when modal is closed

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

  // Function to toggle the modal visibility
  const toggleModal = () => {
    setShowModal(!showModal);
  };

  // Function to handle modal closure
  const handleCloseModal = () => {
    setShowModal(false); // Close the modal
    setModalClosed(!modalClosed); // Trigger re-render by changing the state
  };

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
      {/* Question list and High Scores */}
      <Row>
        <Col md={8}>
          {/* Question List component */}
          <QuestionList
            filteredQuestions={questions} // Pass filtered questions directly
            fetchQuestions={fetchQuestions}
            deleteQuestion={deleteQuestion}
            updateQuestion={updateQuestion}
            toggleModal={toggleModal} // Pass toggleModal function to open/close modal
          />
        </Col>
        <Col md={4}>
          {/* High Scores component */}
          <HighScores showModal={showModal} onCloseModal={handleCloseModal} refreshScores={modalClosed} /> {/* Pass onCloseModal and refreshScores props */}
        </Col>
      </Row>
    </Container>
  );
}

export default App;
