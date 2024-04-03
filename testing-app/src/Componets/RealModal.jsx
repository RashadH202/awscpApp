import React from 'react';
import { Modal, Button } from 'react-bootstrap';

const RealModal = ({ show, handleClose, selectedQuestions }) => {
  return (
    <Modal show={show} onHide={handleClose}>
      {/* Modal Header */}
      <Modal.Header closeButton>
        <Modal.Title>Real Practice Test</Modal.Title>
      </Modal.Header>
      {/* Modal Body */}
      <Modal.Body>
        <ul>
          {/* Map through selected questions and render them */}
          {selectedQuestions.map(question => (
            <li key={question.id}>{question.text}</li>
          ))}
        </ul>
      </Modal.Body>
      {/* Modal Footer */}
      <Modal.Footer>
        {/* Close button */}
        <Button variant="secondary" onClick={handleClose}>
          Close
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default RealModal;
