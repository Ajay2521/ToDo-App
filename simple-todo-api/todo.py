from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
    
# Initialize FastAPI application
app = FastAPI()

# Define a Pydantic model for creating a Todo item
'''
Validation: Ensures title is a string and completed is a boolean. If a client sends data with incorrect types (e.g., "completed": "yes"), FastAPI will reject it.
Serialization/Deserialization: Automatically converts JSON data into a TodoCreate instance and vice versa.
Documentation: The API documentation will show that title must be a string and completed must be a boolean, helping users understand the API requirements.
'''
# define a new class, TodoCreate, which inherits from BaseModel
class TodoCreate(BaseModel):
    title: str
    completed: bool

# Define a Pydantic model for Todo items including the 'id' field
class Todo(TodoCreate):
    id: int

# In-memory storage for Todo items
# Type Hinting (List[Todo]):
todos: List[Todo] = []

# define an endpoint that responds to GET requests at the /todos URL.
@app.get('/todos', response_model=List[Todo])
def get_all():
    """
    Retrieve all Todo items.

    This endpoint handles GET requests to the '/todos' URL. It returns a list of all Todo items currently 
    stored in the `todos` list.
    """
    return todos

@app.get('/todos/{id}', response_model=Todo)
def get_by_id(id: int):
    """
    Retrieve a single Todo item by its ID.

    This endpoint handles GET requests to the '/todos/{id}' URL. It searches for a Todo item with the 
    specified ID. If found, it returns the Todo item; otherwise, it raises a 404 error indicating that 
    the Todo item was not found.
    
    Parameters:
    - id (int): The ID of the Todo item to retrieve.
    
    Returns:
    - Todo: The Todo item with the specified ID.
    """
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post('/todos', response_model=Todo, status_code=201)
def create(req: TodoCreate):
    """
    Create a new Todo item.

    This endpoint handles POST requests to the '/todos' URL. It accepts a Todo item (excluding the ID) 
    in the request body, assigns it a new ID, adds it to the `todos` list, and returns the created 
    Todo item.
    
    Parameters:
    - todo_create (TodoCreate): The Todo item data (title and completed status) to be created.
    
    Returns:
    - Todo: The newly created Todo item including its assigned ID.
    """
    new_id = len(todos) + 1
    new_todo = Todo(id=new_id, **req.model_dump())
    todos.append(new_todo)
    return new_todo

@app.put('/todos/{id}', response_model=Todo)
def update_by_id(id: int, req: TodoCreate):
    """
    Update an existing Todo item by its ID.

    This endpoint handles PUT requests to the '/todos/{id}' URL. It searches for a Todo item with the 
    specified ID, updates its title and completed status with the new values from the request body, 
    and returns the updated Todo item. If the Todo item is not found, it raises a 404 error.
    
    Parameters:
    - id (int): The ID of the Todo item to update.
    - updated_todo (TodoCreate): The new values for the Todo item.
    
    Returns:
    - Todo: The updated Todo item.
    """
    for todo in todos:
        if todo.id == id:
            todo.title = req.title
            todo.completed = req.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete('/todos/{id}', status_code=204)
def delete_by_id(id: int):
    """
    Delete a Todo item by its ID.

    This endpoint handles DELETE requests to the '/todos/{id}' URL. It searches for a Todo item with 
    the specified ID and removes it from the `todos` list. If the Todo item is not found, it raises 
    a 404 error.
    
    Parameters:
    - id (int): The ID of the Todo item to delete.
    
    Returns:
    - None: If the Todo item is successfully deleted, the response has a 204 status code with no content.
    """
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return
    raise HTTPException(status_code=404, detail="Todo not found")

# Entry point to run the application
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000)
