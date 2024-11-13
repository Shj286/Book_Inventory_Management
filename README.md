Book Inventory Management System

This is a simple book inventory management system built with Python (Flask), SQLite, HTML, and CSS. It allows users to add, filter, and export books to a CSV file. The project includes a basic UI that is responsive and easy to use.

Table of Contents

Features
Technologies Used
Project Structure
Setup Instructions
Running the Application
Usage
Design Decisions
Features

Add New Book: Allows users to add a new book with details such as title, author, genre, publication date, and ISBN.
Filter Books: Users can filter books based on title, author, or genre to find specific entries.
Export Books as CSV: Allows users to export the entire book inventory as a CSV file.
Responsive UI: The application includes a responsive user interface that works well on both desktop and mobile screens.
Technologies Used

Backend: Flask, Flask-SQLAlchemy
Database: SQLite
Frontend: HTML, CSS
Export: CSV format
Project Structure

Book_Project/
├── app.py             # Main application file
├── table.sql          # SQL script to create the database table
├── static/
│   └── style.css      # CSS for styling the UI
└── templates/
    └── frontend.html  # HTML template for the UI
Setup Instructions

Follow these steps to set up and run the application:

Prerequisites

Python 3.8 or higher installed
Git (optional but recommended for version control)

Step 1: Clone the Repository
If you've created a repository on GitHub, clone it with the following command:

git clone https://github.com/yourusername/Book_Inventory_Management.git
Or, if you're working locally, just navigate to the project folder in your terminal.

Step 2: Navigate to the Project Directory
cd Book_Project

Step 3: Create a Virtual Environment
It's recommended to create a virtual environment for the project to manage dependencies.

python -m venv env

Step 4: Activate the Virtual Environment
On macOS/Linux:
source env/bin/activate
On Windows:
env\Scripts\activate

Step 5: Install Required Packages
Install the required Python packages from within the virtual environment:

pip install Flask Flask-SQLAlchemy

Step 6: Set Up the Database
Create the SQLite database and Inventory table:

Run the table.sql script manually in an SQLite client, OR
Let db.create_all() in app.py handle it automatically when you run the application.
You can also create the database by running this command in Python:

python -c "from app import db; db.create_all()"

Running the Application

Once the setup is complete, you can start the Flask server and run the application.

Step 1: Start the Flask Application
python app.py
The server will start, and you should see output indicating that Flask is running. The application will be available at http://127.0.0.1:5000.

Step 2: Open the Application in a Web Browser
Open your browser and go to http://127.0.0.1:5000 to see the application interface.

Usage

Add Book: Enter book details in the "Add Book" form and click "Add Book" to save it in the inventory.
Filter Books: Use the filter form to search for books by title, author, or genre.
Export CSV: Click "Export as CSV" to download the book inventory as a CSV file.
Screenshots (optional)
Include screenshots of the application UI, if desired, to make the README more visual.

Design Decisions

Application Logic in Python: The database logic is handled in application code instead of stored procedures for better flexibility.
Responsive UI: The UI is designed with responsive CSS to ensure it works well on both desktop and mobile screens.
Export Format: The book data is exported in CSV format, a widely used and easily readable format.

Challenges Faced

Unique Constraints: Ensuring ISBNs are unique and handling errors if duplicates are entered.
UI Design: Making the UI intuitive and visually appealing with basic HTML and CSS.
Database Context: Handling database initialization within the Flask application context.

Future Enhancements

Add user authentication to protect data access.
Include more filtering options, like filtering by publication date.
Implement pagination for displaying large inventories.
