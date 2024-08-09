## Todo Application

### Overview

This project comprises a Todo application with two main components:

**Backend:** A FastAPI-based REST API for managing Todo items.

**Frontend:** A React application for interacting with the Todo API.

### Features

**Backend:**

- Create, retrieve, update, and delete Todo items.

- Modular architecture following MVC principles.

- Unit tests for backend components.

**Frontend:**

- Add, toggle, and delete Todo items.

-Interfaces with the backend API for data persistence.

### File Structure

```
ToDo-App/
│
├── todo/
│   ├── app/
│   │   ├── controller/
│   │   ├── models/
│   │   ├── repo/
│   │   ├── routes/
│   │   └── service/
│   ├── main.py
│   └── tests/
│
├── react-app/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
└── README.md

```

## Backend Setup and Installation

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

## Frontend Setup and Installation

### Prerequisites

- Node.js (recommended version: 14.x or later)
- npm or yarn

### Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/Ajay2521/ToDo-App.git
    cd ToDo-App/react-app
    ```

2. **Install dependencies:**

    ```
    npm install
    ```

    or if using Yarn:

    ```
    yarn install
    ```

3. **Run the application:**

    ```
    npm start
    ```

    or if using Yarn:

    ```
    yarn start
    ```

### Sample Recording

#### Postman

[postman rec.webm](https://github.com/user-attachments/assets/309d5c53-8167-4e46-a862-a2e7bb864af0)
