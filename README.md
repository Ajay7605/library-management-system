# Library Management System API

This is a Flask-based API for managing books and members in a Library Management System. It supports CRUD operations for books and members, pagination, search functionality, and token-based authentication.

## Features

- CRUD Operations for books and members.
- Search for books by title or author.
- Pagination to retrieve books in pages.
- Token-based Authentication to secure API endpoints.

## Requirements

- Python 3.8+
- Flask


## Setup and Installation

### 1. Clone the repository:
```bash
git clone https://github.com/Ajay7605/library-management-system.git
cd library-management-system


2.Install the dependencies:
    Make sure you have Python 3.8+ installed. Then install the required dependencies by running:
    
    pip install Flask



3.Run the application:
    To start the Flask server, run the following command:

    python app.py

4.Generating a Token
    To generate a token, you need to run the shh.py script with the following command:

    python shh.py

    and the username : 'ajay'

5.API Endpoints

    Books Endpoints

    For each request you make, include the following headers in Postman

    Authorization  -> Generated token
    Username       -> ajay

    Add these headers in the Headers tab of Postman for all requests


6.CRUD Operations

    1.Add a New Book
        Endpoint: POST /books
        Headers: Add the Authorization and Username headers as mentioned above.

        Body (JSON):

            {
                "title": "Flask Assignment",
                "author": "ajay",
                "published_year": 2024
            }
        
        Expected Response: 

        {
            "message": "Book added successfully"
        }

        ex: URL: http://127.0.0.1:5000/books


    2.Get All Books

    Endpoint: GET /books

    Headers: Add the Authorization and Username headers.

    Example Request in Postman:
    URL: http://127.0.0.1:5000/books

    3.Update a Book
        Endpoint: PUT /books/<id>

        Replace <id> with the ID of the book you want to update.
        Headers: Add the Authorization and Username headers.

        Body (JSON):
            {
                "title": "Flask Assignment",
                "author": "ajay",
                "published_year": 2025
            }   
    
    4.Delete a Book
        Endpoint: DELETE /books/<id>

        Replace <id> with the ID of the book you want to delete.
        Headers: Add the Authorization and Username headers.

        Example Request:
        URL: http://127.0.0.1:5000/books/1

    5. Search for a Book
        Endpoint: GET /books/search

        Headers: Add the Authorization and Username headers.

        Query Parameters:

        query: The search keyword (title or author).
        Example Request in Postman:
        URL: http://127.0.0.1:5000/books/search?query=flask









