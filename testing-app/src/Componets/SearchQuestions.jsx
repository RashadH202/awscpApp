import React from 'react';
import { Form } from 'react-bootstrap';

const SearchQuestions = ({ handleSearchInputChange, searchQuery }) => {
  return (
    <div className='search-container-comp'>
     
      <Form.Group controlId="search">
        <Form.Label>Search questions...</Form.Label>
        <Form.Control
          type="text"
          placeholder="Search questions..."
          value={searchQuery}
          onChange={handleSearchInputChange}
        />
      </Form.Group>
    </div>
  );
};

export default SearchQuestions;