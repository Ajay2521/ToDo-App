from fastapi import HTTPException
from typing import List
from app.service import todo_service  # Importing all functions from service
from app.models.todo import TodoCreate, Todo

def get_all() -> List[Todo]:
    return todo_service.get_all()  # Using imported function

def get_by_id(todo_id: int) -> Todo:
    try:
        return todo_service.get_by_id(todo_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Todo not found")

def create(todo_create: TodoCreate) -> Todo:
    return todo_service.create(todo_create)  # Using imported function

def update_by_id(todo_id: int, todo_create: TodoCreate) -> Todo:
    try:
        return todo_service.update_by_id(todo_id, todo_create)
    except ValueError:
        raise HTTPException(status_code=404, detail="Todo not found")

def delete_by_id(todo_id: int) -> None:
    try:
        todo_service.delete_by_id(todo_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Todo not found")