# Console-Based Todo Application

This is a simple console-based Todo application built with Python. The application allows users to manage their tasks by creating, viewing, updating, and deleting Todos directly from the command line.

## Features

- **Create Todos:** Add new tasks with a title and completion status.
- **View All Todos:** Display all tasks with their details.
- **View Todo By ID:** Search and display a task using its unique identifier.
- **Update Todos:** Modify the title and completion status of an existing task.
- **Delete Todos:** Remove a task from the list using its ID.
- **Simple Menu Interface:** Easy-to-use console menu for interacting with the Todo list.

## Installation

### Prerequisites

- Python 3.x

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ajay2521/ToDo-App.git
   cd ToDo-App/console-todo-app
   ```

2. **Run the application:**
   ```python3 todo_app.py```

   This will start the application and display a menu for managing your Todos.

### How to Use

1. **Start the application:**

   Once you run the application, you will be greeted with a menu offering different options.

2. **Choose an option:**

   Enter the number corresponding to the action you want to perform (e.g., 1 to view all Todos, 3 to add a new Todo).

3. **Interact with the Todos:**

   Follow the prompts to perform actions like adding a new Todo, viewing Todos, updating, or deleting them.

4. **Exit the application:**
   
   To exit, select the option 6 from the menu.

### Code Structure

- **Todo Class:** Represents a single task with attributes for ID, title, and completion status.
- **todos List:** Stores all Todo objects.
- Functions:
   - **getAll():** Fetch all Todos.
   - **getByID(id):** Retrieve a Todo by its ID.
   - **create(title, completed):** Create and add a new Todo.
   - **updateByID(id, title, completed):** Update an existing Todo.
   - **deleteByID(id):** Delete a Todo by its ID.
   - **printToDos():** Print all Todos.
   - **printToDo():** Print a specific Todo's details.

#### Contributing
   Feel free to fork this repository and contribute by submitting a pull request.

#### License
   This project is licensed under the MIT License.

#### Contact

   For any questions or feedback, please reach out to [ajay.m.200521@example.com].
