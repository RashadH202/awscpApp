import React from 'react';
import { Modal, Button } from 'react-bootstrap';

const RealModal = ({ show, handleClose, selectedQuestions }) => {
  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Real Practice Test</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <ul>
          {selectedQuestions.map(question => (
            <li key={question.id}>{question.text}</li>
          ))}
        </ul>
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          Close
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default RealModal;
