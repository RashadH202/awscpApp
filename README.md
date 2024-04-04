# AWSCP High Score App

## Overview
The AWSCP High Score App is a serverless web application built on AWS Lambda, API Gateway, DynamoDB, Flask, React, and Bootstrap. It allows users to manage high scores for a game and perform various CRUD operations on questions and high scores.

## Features
- Retrieve, create, update, and delete questions
- Search questions based on keywords
- Retrieve high scores
- Add new high scores
- Simple status check endpoint
- Frontend interface built with React and Bootstrap for a user-friendly experience

## Technologies Used
- **AWS Lambda**: Serverless compute service used to execute application logic
- **Amazon API Gateway**: Fully managed service to create, deploy, and manage APIsgit
- **Amazon DynamoDB**: Fully managed NoSQL database service used to store questions and high scores
- **Flask**: Micro web framework for building web applications in Python
- **React**: JavaScript library for building user interfaces
- **Bootstrap**: Front-end framework for developing responsive and mobile-first websites
- **axios**: Promise-based HTTP client for making API requests from React frontend
- **React Bootstrap**: UI framework for React applications
- **HTML/CSS**: Markup and styling languages for web development
- **JavaScript (ES6+)**: Programming language used for React components and application logic
- **Python**: Programming language used for Flask backend

## Setup
1. Clone the repository: `git clone https://github.com/RashadH202/awscpApp`
2. Navigate to the `backend` directory and follow the setup instructions in the backend README
3. Navigate to the `frontend` directory
4. Install dependencies: `npm install`
5. Start the React app: `npm start`
6. Access the application at `http://localhost:3000`

## Usage
- **Backend Endpoints**:
  - **GET /questions**: Retrieve all questions
  - **POST /questions**: Create a new question
  - **PATCH /questions/{id}**: Update an existing question by ID
  - **DELETE /questions/{id}**: Delete a question by ID
  - **GET /questions/search**: Search questions by keyword
  - **GET /status**: Perform a simple status check
  - **GET /highscores**: Retrieve all high scores
  - **POST /highscores**: Add a new high score
- **React Frontend**:
  - Access the web application through the browser
  - View, create, update, and delete questions
  - Search for questions by keyword
  - View high scores and add new high scores

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new pull request

## License
This project is licensed under the MIT License -

## Acknowledgements
- Thanks to the AWS Cloud Practitioner team for inspiration and guidance.
