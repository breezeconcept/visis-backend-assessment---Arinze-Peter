# Text Summarizer Backend

This project is a backend service for a text summarizer application. It uses FastAPI to create RESTful APIs and SQLAlchemy for database interactions. The backend can handle book information requests and summary generation using the OpenAI API.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- Add, retrieve, update, and delete book information.
- Generate summaries for book texts using the OpenAI API.

## Requirements

- Python 3.8+
- PostgreSQL database

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/text-summarizer-backend.git
    cd text-summarizer-backend
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv ENV
    source ENV/bin/activate  # On Windows, use `ENV\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. **Create a `.env` file** in the root directory and add the following environment variables:

    ```env
    DATABASE_URL=postgresql://user:password@localhost/dbname
    OPENAI_API_KEY=your-openai-api-key
    ```

2. **Update `app/core/config.py`** if you have additional configuration needs.

## Running the Application

1. **Run the database migrations**:
    ```sh
    alembic upgrade head
    ```

2. **Start the FastAPI application**:
    ```sh
    uvicorn app.main:app --reload
    ```

3. **Access the API documentation**:
    Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

## API Endpoints

### Books

- **Create a Book**
    ```http
    POST /api/books
    ```
    - Request Body:
        ```json
        {
            "title": "Book Title",
            "publisher": "Publisher Name",
            "text": "Full text of the book",
            "summary": "Summary of the book"
        }
        ```
    - Response:
        ```json
        {
            "id": "book-id",
            "title": "Book Title",
            "publisher": "Publisher Name",
            "text": "Full text of the book",
            "summary": "Summary of the book"
        }
        ```

- **Get All Books**
    ```http
    GET /api/books
    ```
    - Response:
        ```json
        [
            {
                "id": "book-id",
                "title": "Book Title",
                "publisher": "Publisher Name",
                "text": "Full text of the book",
                "summary": "Summary of the book"
            },
            ...
        ]
        ```

- **Get a Book by ID**
    ```http
    GET /api/books/{book_id}
    ```
    - Response:
        ```json
        {
            "id": "book-id",
            "title": "Book Title",
            "publisher": "Publisher Name",
            "text": "Full text of the book",
            "summary": "Summary of the book"
        }
        ```

- **Update a Book**
    ```http
    PUT /api/books/{book_id}
    ```
    - Request Body:
        ```json
        {
            "title": "Updated Book Title",
            "publisher": "Updated Publisher Name",
            "text": "Updated full text of the book",
            "summary": "Updated summary of the book"
        }
        ```
    - Response:
        ```json
        {
            "id": "book-id",
            "title": "Updated Book Title",
            "publisher": "Updated Publisher Name",
            "text": "Updated full text of the book",
            "summary": "Updated summary of the book"
        }
        ```

- **Delete a Book**
    ```http
    DELETE /api/books/{book_id}
    ```
    - Response:
        ```json
        {
            "message": "Book deleted successfully"
        }
        ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
