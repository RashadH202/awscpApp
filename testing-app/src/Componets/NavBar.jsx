import React from 'react';
import { Navbar, Nav, Form } from 'react-bootstrap';
import AddQuestionModal from './AddQuestionModal';
import SearchQuestions from './SearchQuestions';
import TestGenerator from './TestGenerator';
import RealTestGenerator from './RealTesetGenerator';
import QuestionCount from './QuestionCount'; // Import the QuestionCount component

const NavBar = ({ fetchQuestions, handleSearchInputChange, searchQuery, questionCount }) => {
    return (
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand href="#home">AWSCP Practice Test</Navbar.Brand>
            <Nav className="mr-auto">
                <AddQuestionModal fetchQuestions={fetchQuestions} />
            </Nav>
            <Nav >
                <Form inline="true">
                    <SearchQuestions
                        handleSearchInputChange={handleSearchInputChange}
                        searchQuery={searchQuery}
                    />
                </Form>
            </Nav>
            <Nav >
                <Form inline="true">
                    <TestGenerator />
                </Form>
            </Nav>
            <Nav >
                <Form inline="true">
                    <RealTestGenerator />
                </Form>
            </Nav>
            <Nav >
                <QuestionCount count={questionCount} /> {/* Integrate the QuestionCount component */}
            </Nav>
        </Navbar>
    );
};

export default NavBar;
