import React, { useState } from 'react';
import { Modal, Button } from 'react-bootstrap';
import AddQuestion from './AddQuestion'; // Import your AddQuestion component

const AddQuestionModal = ({ fetchQuestions }) => {
  // State to manage the visibility of the modal
  const [show, setShow] = useState(false);

  // Function to close the modal
  const handleClose = () => setShow(false);

  // Function to open the modal
  const handleShow = () => setShow(true);

  return (
    <>
      {/* Button to open the modal */}
      <Button variant="primary" onClick={handleShow}>
        Add Question
      </Button>

      {/* Modal component */}
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Add New Question</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {/* Render the AddQuestion component inside the modal */}
          <AddQuestion fetchQuestions={fetchQuestions} />
        </Modal.Body>
        <Modal.Footer>
          {/* Button to close the modal */}
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default AddQuestionModal;
