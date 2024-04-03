import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Row, Col, Button, Modal } from 'react-bootstrap';
import './App.css';
import QuestionList from './Componets/QuestionList';
import HighScores from './Componets/HighScores';
import NavBar from './Componets/NavBar';


function App() {
  // State variables
  const [questions, setQuestions] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [modalClosed, setModalClosed] = useState(false);


  // Fetch questions from the backend when the component mounts
  useEffect(() => {
    fetchQuestions();
  }, [modalClosed]); // Refetch questions when modal is closed

  // Fetch questions from the backend
  const fetchQuestions = async () => {
    try {
      console.log('Fetching questions...');
      const response = await axios.get('https://52ngda61vl.execute-api.us-east-1.amazonaws.com/default/questions');
      console.log('Questions fetched successfully:', response.data);
      setQuestions(response.data);
    } catch (error) {
      console.error('Error fetching questions:', error);
    }
  };


  // Handle changes in the search input
  const handleSearchInputChange = (e) => {
    setSearchQuery(e.target.value);
  };

  // Filter questions based on search query
  const filteredQuestions = questions.filter(question =>
    question.question.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Function to toggle the modal visibility
  const toggleModal = () => {
    setShowModal(!showModal);
  };

  // Function to handle modal closure
  const handleCloseModal = () => {
    setShowModal(false); // Close the modal
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
            questionCount={questions.length}
          />
        </Col>
      </Row>
      {/* Question list and High Scores */}
      <Row>
        <Col md={8}>
          {/* Question List component */}
          <QuestionList
            filteredQuestions={filteredQuestions} // Pass filtered questions
            fetchQuestions={fetchQuestions}
          />
        </Col>
        <Col md={4}>
          {/* High Scores component */}
          <HighScores showModal={showModal} onCloseModal={handleCloseModal} refreshScores={modalClosed} />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
