import React, { useState } from 'react';
import { Modal, Button } from 'react-bootstrap';
import AddQuestion from './AddQuestion'; // Import your AddQuestion component

const AddQuestionModal = ({ fetchQuestions }) => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <>
      <Button variant="primary" onClick={handleShow}>
        Add Question
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Add New Question</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <AddQuestion fetchQuestions={fetchQuestions} />
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default AddQuestionModal;
