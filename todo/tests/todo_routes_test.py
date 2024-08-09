import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from fastapi import FastAPI,  HTTPException
from app.routes.todo_routes import todo_router
from app.models.todo import Todo

app = FastAPI(
    title="Todo API",
    description="A simple API for managing Todo items.",
    version="1.0.0"
)

# Include the Todo routes
app.include_router(todo_router)

client = TestClient(app)

class TestTodoRoutes(unittest.TestCase):

    @patch('app.controller.todo_controller.get_all')
    def test_get_all_todos_success(self, mock_get_all):
        mock_get_all.return_value = [
            Todo(id=1, title="Test Todo 1", completed=False),
            Todo(id=2, title="Test Todo 2", completed=True)
        ]
        response = client.get('/todos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    @patch('app.controller.todo_controller.get_by_id')
    def test_get_todo_by_id_success(self, mock_get_by_id):
        mock_get_by_id.return_value = Todo(id=1, title="Test Todo", completed=False)
        response = client.get('/todos/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)

    @patch('app.controller.todo_controller.get_by_id')
    def test_get_todo_by_id_not_found(self, mock_get_by_id):
        mock_get_by_id.side_effect = HTTPException(status_code=404, detail="Todo not found")
        response = client.get('/todos/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['detail'], "Todo not found")

    @patch('app.controller.todo_controller.create')
    def test_create_todo_success(self, mock_create):
        todo_data = {"title": "New Todo", "completed": False}
        mock_create.return_value = Todo(id=1, **todo_data)
        response = client.post('/todos', json=todo_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 1)
        self.assertEqual(response.json()['title'], "New Todo")

    @patch('app.controller.todo_controller.create')
    def test_create_todo_invalid_data(self, mock_create):
        todo_data = {"title": 123, "completed": "invalid"}
        response = client.post('/todos', json=todo_data)
        self.assertEqual(response.status_code, 422)

    @patch('app.controller.todo_controller.update_by_id')
    def test_update_todo_by_id_success(self, mock_update_by_id):
        todo_data = {"title": "Updated Todo", "completed": True}
        mock_update_by_id.return_value = Todo(id=1, **todo_data)
        response = client.put('/todos/1', json=todo_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], "Updated Todo")

    @patch('app.controller.todo_controller.update_by_id')
    def test_update_todo_by_id_not_found(self, mock_update_by_id):
        mock_update_by_id.side_effect = HTTPException(status_code=404, detail="Todo not found")
        todo_data = {"title": "Updated Todo", "completed": True}
        response = client.put('/todos/999', json=todo_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['detail'], "Todo not found")

    @patch('app.controller.todo_controller.delete_by_id')
    def test_delete_todo_by_id_success(self, mock_delete_by_id):
        response = client.delete('/todos/1')
        self.assertEqual(response.status_code, 204)

    @patch('app.controller.todo_controller.delete_by_id')
    def test_delete_todo_by_id_not_found(self, mock_delete_by_id):
        mock_delete_by_id.side_effect = HTTPException(status_code=404, detail="Todo not found")
        response = client.delete('/todos/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['detail'], "Todo not found")

if __name__ == '__main__':
    unittest.main()