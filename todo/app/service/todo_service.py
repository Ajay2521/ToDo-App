from app.repo import todo_repo  # Importing all functions from repo
from typing import List
from app.models.todo import Todo, TodoCreate

def get_all() -> List[Todo]:
    return todo_repo.get_all()  # Using imported function

def get_by_id(todo_id: int) -> Todo:
    todo = todo_repo.get_by_id(todo_id)
    if not todo:
        raise ValueError("Todo not found")
    return todo

def create(todo_create: TodoCreate) -> Todo:
    new_id = len(todo_repo.get_all()) + 1
    new_todo = Todo(id=new_id, **todo_create.model_dump())
    todo_repo.create(new_todo)
    return new_todo

def update_by_id(todo_id: int, todo_create: TodoCreate) -> Todo:
    updated_todo = Todo(id=todo_id, **todo_create.model_dump())
    if not todo_repo.update_by_id(todo_id, updated_todo):
        raise ValueError("Todo not found")
    return updated_todo

def delete_by_id(todo_id: int) -> None:
    if not todo_repo.delete_by_id(todo_id):
        raise ValueError("Todo not found")