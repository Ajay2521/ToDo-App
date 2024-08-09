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

    ```
   git clone https://github.com/Ajay2521/ToDo-App.git
   cd ToDo-App/simple-todo-api
    ```

2. To run the FastAPI application:

    ```
    python run main.py
    ```
    
    ```
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
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
```
