# Todo Application with FastAPI

## Overview

This project is a FastAPI-based application for managing Todo items. It demonstrates a modular architecture following the MVC (Model-View-Controller) principles and includes unit tests to verify the functionality of various components.

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
    cd ToDo-App/todo
    ```

2. To run the FastAPI application:

    ```
    python run main.py
    ```
    
    ```
    uvicorn main:app --reload
    ```

    This command starts the FastAPI application on `http://127.0.0.1:8000` with auto-reload enabled for development.

### Testing

**Unit Testing**

To run unit tests for the FastAPI backend:    

```
python -m unittest -s tests -p '*_test.py'
```

Discover and run all unit tests in the app directory that match the pattern *_test.py.

 
**Test Coverage**

Run tests with coverage:

```
python -m coverage run -m unittest discover
```

or

```
python -m coverage run -m unittest discover -s tests -p '*_test.py'
```

Runs unit tests and collects coverage data.

**Generate a coverage report:**

```
python -m coverage report
```

Displays the coverage report in the terminal.

**Generate an HTML coverage report:**

```
python -m coverage html
```

Creates an HTML report of the coverage data. Open `htmlcov/index.html` in a web browser to view it.


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


### File Structure

```
app/
│
├── controller/
│   └── todo_controller.py       # Handles business logic and interacts with the service layer
│
├── models/
│   └── todo.py                  # Defines Pydantic models for Todo items
│
├── repo/
│   └── todo_repo.py             # In-memory storage and CRUD operations for Todo items
│
├── routes/
│   └── todo_routes.py           # Defines FastAPI routes and connects them to controller functions
│
├── service/
│   └── todo_service.py          # Contains business logic and interacts with the repository layer
│
main.py                          # Entry point of the application
tests/
│
├── todo_controller_test.py      # Unit tests for the todo_controller functions
├── todo_repo_test.py            # Unit tests for the todo_repo functions
├── todo_service_test.py         # Unit tests for the todo_service functions
└── todo_routes_test.py          # Unit tests for the todo_routes functions

```


## File Descriptions

### app/controller/todo_controller.py

**Purpose:** Manages requests and responses related to Todo items. Uses functions from the service layer to perform operations.

**Functions:**

- **get_all():** Retrieves all Todo items.

- **get_by_id(todo_id: int):** Retrieves a Todo item by its ID.

- **create(todo_create: TodoCreate):** Creates a new Todo item.

- **update_by_id(todo_id: int, todo_create: TodoCreate):** Updates an existing Todo item by its ID.

- **delete_by_id(todo_id: int):** Deletes a Todo item by its ID.

### app/models/todo.py

**Purpose:** Defines the data models for Todo items using Pydantic.

**Classes:**

- **TodoCreate:** Model for creating new Todo items (title and completed status).

- **Todo:** Model for Todo items including an ID.

### app/repo/todo_repo.py

**Purpose:** Handles in-memory storage and CRUD operations for Todo items.

**Functions:**

- **get_all():** Retrieves all Todo items from the in-memory storage.

- **get_by_id(todo_id: int):** Retrieves a Todo item by its ID.

- **create(todo: Todo):** Adds a new Todo item to the storage.

- **update_by_id(todo_id: int, updated_todo: Todo):** Updates an existing Todo item by its ID.

- **delete_by_id(todo_id: int):** Deletes a Todo item by its ID.

### app/routes/todo_routes.py

**Purpose:** Defines the API routes and connects them to the appropriate controller functions.

**Routes:**

- **GET /todos:** Retrieves all Todo items.

- **GET /todos/{id}:** Retrieves a Todo item by its ID.

- **POST /todos:** Creates a new Todo item.

- **PUT /todos/{id}:** Updates an existing Todo item by its ID.

- **DELETE /todos/{id}: **Deletes a Todo item by its ID.

### app/service/todo_service.py

**Purpose:** Contains business logic and interacts with the repository layer to perform operations on Todo items.

**Functions:**

- **get_all():** Retrieves all Todo items from the repository.

- **get_by_id(todo_id: int):** Retrieves a Todo item by its ID, raising an error if not found.

- **create(todo_create: TodoCreate):** Creates a new Todo item with a generated ID.

- **update_by_id(todo_id: int, todo_create: TodoCreate):** Updates an existing Todo item by its ID.

- **delete_by_id(todo_id: int):** Deletes a Todo item by its ID.

### main.py

**Purpose:** Entry point of the FastAPI application. Configures middleware and includes API routes.


## Tests

### tests/todo_controller_test.py

**Purpose:** Contains unit tests for functions in todo_controller.py. Uses mocking to test controller logic without depending on the service layer.

### tests/todo_repo_test.py

**Purpose:** Contains unit tests for functions in todo_repo.py. Tests in-memory CRUD operations.

### tests/todo_service_test.py

**Purpose:** Contains unit tests for functions in todo_service.py. Tests business logic and interactions with the repository layer.

### tests/todo_routes_test.py

**Purpose:** Contains unit tests for API routes defined in todo_routes.py. Tests the integration between routes and controller functions.


