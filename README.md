# QuizNova

COMPANY : CODTECH IT SOLUTIONS

NAME : SABREENA

INTERN ID : CTIS05S6

DOMAIN : FULL STACK WEB DEVELOPMENT

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

# QuizNova – Smart Quiz Platform with Leaderboard

## Overview

QuizNova is a dynamic and interactive quiz platform developed using Python and Streamlit. The application is designed to provide users with an engaging environment to test
their knowledge across multiple technical and aptitude-based categories. Unlike traditional quiz systems that present the same set of questions repeatedly, QuizNova
introduces randomness by selecting different questions for every quiz attempt. This ensures a unique experience for users each time they participate.

The platform has been built as a lightweight application without requiring a separate frontend, backend, or database. All functionalities are integrated into a simple
Streamlit-based interface, making the project easy to deploy, maintain, and use. QuizNova is suitable for students, educators, and learners who wish to evaluate their
knowledge while tracking their performance through a leaderboard system.

## Objectives

The primary objective of QuizNova is to create a user-friendly online assessment platform that enables participants to:

* Test their knowledge in various subjects.
  
* Attempt randomized quizzes.
  
* Compete with others through a leaderboard.
  
* Improve learning through repeated practice.
  
* Experience a responsive and interactive quiz environment.

The project demonstrates the practical implementation of Python programming, file handling, data management, randomization techniques, and user interface development using

Streamlit.

## Features

### 1. Multiple Categories

QuizNova provides questions from multiple categories including:

* Python Programming
  
* Java Programming
  
* Database Management Systems (DBMS)
  
* Operating Systems (OS)
  
* Aptitude and Logical Reasoning

Users can select their preferred category before starting the quiz.

### 2. Random Question Selection

The application stores a large collection of questions in a JSON file. Every time a user starts a quiz, the system randomly selects a subset of questions using Python's

`random.sample()` function. This ensures that no two quiz attempts are exactly the same.

### 3. Randomized Answer Options

To increase fairness and prevent memorization of answer positions, the options for each question are shuffled dynamically before being displayed.

### 4. Timer-Based Assessment

QuizNova includes a countdown timer that challenges users to complete the quiz within a specified duration. The timer adds excitement and encourages quick decision-making.

### 5. Automated Score Calculation

After submission, the application automatically evaluates all answers and calculates the final score. The user receives immediate feedback regarding their performance.

### 6. Leaderboard System

The platform maintains a leaderboard that records participant names, scores, categories, and timestamps. This feature promotes healthy competition among users and

motivates them to achieve higher scores.

### 7. Local Data Storage

Instead of relying on a database, QuizNova stores data locally using JSON files. This approach keeps the project simple while demonstrating effective file handling

techniques in Python.

### 8. User-Friendly Interface

The Streamlit framework provides a clean and interactive user interface that allows users to navigate the application effortlessly.

## Technologies Used

The following technologies and tools were used in the development of QuizNova:

* Python
  
* Streamlit
  
* JSON
  
* Random Module
  
* Datetime Module
  
* File Handling

## Working of the Application

When the application starts, the user enters their name and selects a quiz category. Upon clicking the Start Quiz button, the system retrieves all available questions from

the JSON file and randomly selects a predefined number of questions.

Each question is displayed with multiple-choice options. The order of these options is randomized to ensure fairness. A timer begins counting down as soon as the quiz

starts.

After answering all questions, the user submits the quiz. The system compares the submitted answers with the correct answers stored in the question bank and calculates the

score. The result is displayed instantly along with the user's performance statistics.

The score is then saved to the leaderboard file. Users can visit the leaderboard section to view rankings and compare their performance with others.

## Advantages

* Simple and lightweight architecture.
  
* No database installation required.
  
* Easy deployment and maintenance.
  
* Randomized questions improve learning effectiveness.
  
* Encourages competitive learning through leaderboards.
  
* Suitable for educational institutions and self-learning platforms.
  
* Provides practical exposure to Streamlit development.

## Future Enhancements

The project can be further enhanced by adding:

* User authentication and login system.
  
* AI-generated questions.
  
* Difficulty levels (Easy, Medium, Hard).
  
* Performance analytics and charts.
  
* Subject-wise progress tracking.
  
* Online database integration.
  
* Multiplayer quiz competitions.
  
* Certificate generation for top performers.

## Conclusion

QuizNova is an efficient and interactive quiz platform that combines learning with competition. By leveraging Python and Streamlit, the application delivers a complete 
quiz experience without requiring complex infrastructure. The use of randomized questions, timed assessments, category-based quizzes, and leaderboard tracking makes the 
platform engaging and effective for users. This project demonstrates essential software development concepts such as user interaction, data management, randomization, file
handling, and performance evaluation, making it an excellent educational and portfolio project.
