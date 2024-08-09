from fastapi import APIRouter
from typing import List
from app.controller  import todo_controller # Importing all functions from handler
from app.models.todo import Todo, TodoCreate

todo_router = APIRouter()

@todo_router.get('/todos', response_model=List[Todo])
def get_all():
    return todo_controller.get_all()

@todo_router.get('/todos/{id}', response_model=Todo)
def get_by_id(id: int):
    return todo_controller.get_by_id(id)

@todo_router.post('/todos', response_model=Todo, status_code=201)
def create(todo_create: TodoCreate):
    return todo_controller.create(todo_create)

@todo_router.put('/todos/{id}', response_model=Todo)
def update_by_id(id: int, todo_create: TodoCreate):
    return todo_controller.update_by_id(id, todo_create)

@todo_router.delete('/todos/{id}', status_code=204)
def delete_by_id(id: int):
    todo_controller.delete_by_id(id)