import React from 'react';
import { Navbar, Nav, Form, Dropdown } from 'react-bootstrap';
import AddQuestionModal from './AddQuestionModal';
import SearchQuestions from './SearchQuestions';
import TestGenerator from './TestGenerator';
import RealTestGenerator from './RealTesetGenerator';
import QuestionCount from './QuestionCount'; // Import the QuestionCount component

const NavBar = ({ fetchQuestions, handleSearchInputChange, searchQuery, questionCount }) => {
    return (
        <Navbar bg="dark" variant="dark" className="navbar-container">
            {/* Brand name */}
            <Navbar.Brand href="#home">AWSCP Practice Test</Navbar.Brand>
            {/* Left-aligned items */}
            <Nav className="mr-auto">
                <AddQuestionModal className="question-item" fetchQuestions={fetchQuestions} />
            </Nav>
            {/* Right-aligned items */}
            <Nav className="dropdown-menu-container">
                <Form inline="true">
                    {/* Dropdown for all options except search */}
                    <Dropdown>
                        <Dropdown.Toggle variant="primary" className="dropdown-toggle">
                            Menu
                        </Dropdown.Toggle>
                        <Dropdown.Menu className="dropdown-menu">
                            <Dropdown.Item><TestGenerator /></Dropdown.Item>
                            <Dropdown.Item><RealTestGenerator /></Dropdown.Item>
                            <Dropdown.Item><QuestionCount count={questionCount} /></Dropdown.Item>
                        </Dropdown.Menu>
                    </Dropdown>
                </Form>
            </Nav>
            {/* Search bar outside dropdown */}
            <Nav className="search-bar-container">
                <Form inline="true">
                    <SearchQuestions
                        handleSearchInputChange={handleSearchInputChange}
                        searchQuery={searchQuery}
                        className="search-bar"
                    />
                </Form>
            </Nav>
        </Navbar>
    );
};

export default NavBar;
