# Todo React Application

## Overview

This is a Todo application built with React. It provides a simple interface to manage todo items, including functionalities to add, toggle, and delete todos. The application interacts with a backend API (assumed to be running on `http://127.0.0.1:3000`) for data persistence.

## API Endpoints

The application interacts with the following API endpoints:

- **GET `/todos`**: Fetches the list of todos.

- **POST `/todos`**: Adds a new todo.

- **PUT `/todos/{id}`**: Updates an existing todo.

- **DELETE `/todos/{id}`**: Deletes a todo.

## File Structure

The project is organized as follows:

```
src/
├── components/
│ ├── TodoForm.js
│ ├── TodoFormContent.js
│ ├── TodoItem.js
│ ├── TodoList.js
│ └── TodoPage.js
├── App.js
└── index.js
```

### src/components/

#### `TodoForm`

Manages the state of the todo input and handles form submission. It uses `TodoFormContent` for rendering the form.

#### `TodoFormContent`

Contains the UI elements for adding a new todo, including a text input and a submit button.

#### `TodoItem`

Displays individual todo items with options to toggle the completion status and delete the item.

#### `TodoList`

Renders a list of `TodoItem` components based on the provided todos array.

#### `TodoPage`

Handles API interactions (fetching, adding, toggling, and deleting todos) and renders `TodoForm` and `TodoList`.


### src/App.js

- **App.js**: The main component that renders the `TodoPage` component. It serves as the entry point for the application.

### src/index.js

- **index.js**: The entry point for the React application. It renders the `App` component into the DOM element with the id of `root`.

## Setup and Installation

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

    This will start the development server and open the application in your default web browser at `http://localhost:3000`.




