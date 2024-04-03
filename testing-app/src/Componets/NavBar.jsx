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
            {/* Brand name */}
            <Navbar.Brand href="#home">AWSCP Practice Test</Navbar.Brand>
            {/* Left-aligned items */}
            <Nav className="mr-auto">
                {/* AddQuestionModal component */}
                <AddQuestionModal fetchQuestions={fetchQuestions} />
            </Nav>
            {/* Right-aligned items */}
            <Nav >
                <Form inline="true">
                    {/* SearchQuestions component */}
                    <SearchQuestions
                        handleSearchInputChange={handleSearchInputChange}
                        searchQuery={searchQuery}
                    />
                </Form>
            </Nav>
            <Nav >
                <Form inline="true">
                    {/* TestGenerator component */}
                    <TestGenerator />
                </Form>
            </Nav>
            <Nav >
                <Form inline="true">
                    {/* RealTestGenerator component */}
                    <RealTestGenerator />
                </Form>
            </Nav>
            <Nav >
                {/* QuestionCount component */}
                <QuestionCount count={questionCount} />
            </Nav>
        </Navbar>
    );
};

export default NavBar;
