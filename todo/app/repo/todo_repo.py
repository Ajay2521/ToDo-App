from typing import List
from app.models.todo import Todo

# In-memory storage for Todo items
todos: List[Todo] = []

def get_all() -> List[Todo]:
    return todos

def get_by_id(todo_id: int) -> Todo:
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None

def create(todo: Todo) -> None:
    todos.append(todo)

def update_by_id(todo_id: int, updated_todo: Todo) -> bool:
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return True
    return False

def delete_by_id(todo_id: int) -> bool:
    global todos
    original_length = len(todos)
    todos = [todo for todo in todos if todo.id != todo_id]
    return len(todos) < original_length
