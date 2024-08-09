class Todo:
    # The Todo class represents a single task in our Todo application.
    def __init__(self, id, title, completed):
        """ 
        Initialize a new Todo object.

        Args:
        id (int): Unique identifier for the Todo.
        title (str): The title or description of the Todo.
        completed (bool): Status of the Todo (True if completed, False otherwise).
        """
        self.id = id
        self.title = title
        self.completed = completed

# Initialize an empty list to store all Todo objects.
todos = []

def getAll():
    """
    Fetch and return all Todos in the list.
    
    Returns:
    list: A list of all Todo objects.
    """
    if len(todos) == 0:
        print("\nNo todos found.")  # Notify if there are no Todos.
    return todos

def getByID(id):
    """
    Search for and return a Todo by its ID.

    Args:
    id (int): The unique identifier of the Todo to find.

    Returns:
    Todo or None: The Todo object if found, otherwise None.
    """
    for todo in todos:
        if todo.id == id:
            return todo  # Return the Todo if found.
    print(f"\nTodo with ID {id} not found.")  # Notify if the Todo is not found.
    return None

def create(title, completed=False):
    """
    Create a new Todo and add it to the list.

    Args:
    title (str): The title or description of the new Todo.
    completed (bool, optional): Status of the new Todo (default is False).

    Returns:
    Todo: The newly created Todo object.
    """
    new_todo = Todo(len(todos) + 1, title, completed)  # Assign a new ID based on list length.
    todos.append(new_todo)  # Add the new Todo to the list.
    return new_todo

def updateByID(id, title=None, completed=False):
    """
    Update the title and/or completion status of a Todo by its ID.

    Args:
    id (int): The unique identifier of the Todo to update.
    title (str, optional): The new title for the Todo (default is None, meaning no change).
    completed (bool, optional): The new completion status (default is False).

    Returns:
    Todo or None: The updated Todo object if found, otherwise None.
    """
    todo = getByID(id)  # Find the Todo by ID.
    if todo:
        todo.title = title  # Update the title if provided.
        todo.completed = completed  # Update the completed status.
        return todo  # Return the updated Todo.
    return None

def deleteByID(id):
    """
    Delete a Todo by its ID.

    Args:
    id (int): The unique identifier of the Todo to delete.

    Returns:
    Todo or None: The deleted Todo object if found, otherwise None.
    """
    todo = getByID(id)  # Find the Todo by ID.
    if todo:
        todos.remove(todo)  # Remove the Todo from the list.
        return todo  # Return the deleted Todo.
    return None

def printToDos():
    """
    Print the details of all Todos.
    """
    for todo in getAll():  # Iterate over all Todos.
        printToDo(todo)  # Print details of each Todo.

def printToDo(todo):
    """
    Print the details of a single Todo.

    Args:
    todo (Todo): The Todo object whose details are to be printed.
    """
    print(f"\nTodo ID: {todo.id}, Title: {todo.title}, Completed: {todo.completed}")

def main():
    """
    Main function to run the Todo application.
    Provides a menu to interact with the Todo list.
    """
    print("Welcome to Todo App!")  # Greet the user.
    while True:
        # Display menu options for interacting with the Todo list.
        print("\nChoose an option:")
        print("1. View Todos")
        print("2. View Todo By Id")
        print("3. Add Todo")
        print("4. Update Todo")
        print("5. Delete Todo")
        print("6. Exit")

        # Get the user's choice from the menu.
        choice = input("Enter your choice: ")
        
        if choice == '1':
           # View all Todos.
           printToDos()
        
        elif choice == '2':
            # View a specific Todo by its ID.
            id = int(input("Enter todo ID to get: "))
            getByID(id)
        
        elif choice == '3':
            # Add a new Todo.
            title = input("Enter todo title: ")
            completed = input("Is it completed? (True/False): ") 
            printToDo(create(title, completed.lower() == 'true'))  # Ensure the completion status is boolean.
        
        elif choice == '4':
            # Update an existing Todo by its ID.
            id = int(input("Enter todo ID to update: "))
            title = input("Enter new title (press enter to skip): ")
            completed = input("Is it completed? (press enter to skip): ")
            todo = updateByID(id, title, completed.lower() == 'true')
            if todo:
                printToDo(todo)
        
        elif choice == '5':
            # Delete a Todo by its ID.
            todo_id = int(input("Enter todo ID to delete: "))
            deleted_todo = deleteByID(todo_id)
            if deleted_todo:
                print(f"\nDeleted Todo ID: {deleted_todo.id}")
        
        elif choice == '6':
            # Exit the application.
            print("\nExiting...")
            break
        
        else:
            # Handle invalid menu options.
            print("\nInvalid choice. Please try again.")

# Ensure that the main function runs only if this script is executed directly.
# is used to determine whether the Python file is being run as the main program or if it is being imported as a module in another file.
if __name__ == '__main__':
    main()
