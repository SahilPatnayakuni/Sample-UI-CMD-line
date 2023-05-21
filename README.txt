Video Game Review Emotion Aggregator

This project aims to create a web-based video game review aggregator using Flask, React, and SQL. The application allows users to browse and search for video game reviews based on emotions and provides an aggregated rating for each game.
Features

    User Registration and Authentication: Users can create accounts, log in, and manage their profiles.
    Game Search: Users can search for games by title, genre, or platform.
    Review Aggregation: The application collects reviews from different sources and calculates an aggregated rating for each game.
    User Reviews: Registered users can write their own reviews and rate games. Reviews must include an emotional rating for the following emotions (Happy, Sad, Angry, Fearful, Disgust)
    Sorting and Filtering: Users can sort and filter game reviews based on various criteria such as rating, release date, and platform.
    Social Features: Users can follow other users, like and comment on reviews, and share reviews on social media platforms.

Technologies Used

    Backend: Flask (Python)
    Frontend: React (JavaScript)
    Database: SQL (e.g., PostgreSQL, MySQL)

Prerequisites

To run this project locally, ensure you have the following software installed:

    Python 3.x
    SQL database server (e.g., PostgreSQL)

Getting Started

    Clone the repository:

bash

git clone https://github.com/your-username/Video-Game-Review-Emotion.git

    Set up the backend:
        Navigate to the backend directory: cd video-game-review-aggregator/backend
        Create a virtual environment: python3 -m venv venv
        Activate the virtual environment:
            On macOS/Linux: source venv/bin/activate
            On Windows: venv\Scripts\activate.bat
        Install the required Python packages: pip install -r requirements.txt
        Set up the database:
            Create a new database in your SQL server.
            Update the database configuration in config.py.
            Run database migrations: flask db upgrade
        Start the backend server: flask run

    Set up the frontend:
        Navigate to the frontend directory: cd video-game-review-aggregator/frontend
        Install the required Node packages: npm install
        Start the frontend development server: npm start

    Access the application:
        Open your web browser and visit http://localhost:3000 to access the video game review aggregator.
