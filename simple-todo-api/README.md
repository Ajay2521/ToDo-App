# Todo Application with FastAPI

## Overview

This is a simple Todo application built with Python's FastAPI framework. It includes endpoints for managing Todo items using CRUD operations. The application supports creating, retrieving, updating, and deleting Todo items. It also features basic validation, serialization, and documentation using FastAPI's built-in tools.

## Features

- Create a Todo item
- Retrieve all Todo items
- Retrieve a Todo item by ID
- Update a Todo item by ID
- Delete a Todo item by ID

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/todo-app.git
    cd todo-app
    ```

2. To run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

    This command starts the FastAPI application on `http://127.0.0.1:8000` with auto-reload enabled for development.

### API Endpoints

- **GET /todos:** Retrieve all Todo items.

- **GET /todos/{id}:** Retrieve a single Todo item by its ID.

- **POST /todos:** Create a new Todo item.

- **PUT /todos/{id}:** Update an existing Todo item by its ID.

- **DELETE /todos/{id}:** Delete a Todo item by its ID.

### API Documentation

FastTrack Todo uses Swagger UI for API documentation. Access it at:

```
Swagger UI: http://127.0.0.1:5000/docs

ReDoc: http://127.0.0.1:5000/redoc
```

### Testing

**Unit Testing**

To run unit tests for the FastAPI backend:    

```
python3 -m unittest -s tests -p '*_test.py'
```

Discover and run all unit tests in the app directory that match the pattern *_test.py.

 
**Test Coverage**

Run tests with coverage:

```
python3 -m coverage run -m unittest discover
```

or

```
python3 -m coverage run -m unittest discover -s tests -p '*_test.py'
```

Runs unit tests and collects coverage data.

**Generate a coverage report:**

```
python3 -m coverage report
```

Displays the coverage report in the terminal.

**Generate an HTML coverage report:**

```
python3 -m coverage html
```

Creates an HTML report of the coverage data. Open `htmlcov/index.html` in a web browser to view it.
