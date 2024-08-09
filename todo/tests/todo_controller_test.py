import unittest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from app.controller.todo_controller import get_all, get_by_id, create, update_by_id, delete_by_id
from app.models.todo import TodoCreate, Todo

class TestController(unittest.TestCase):

    @patch('app.service.todo_service.get_all')
    def test_get_all_success(self, mock_get_all):
        # Arrange
        mock_get_all.return_value = [Todo(id=1, title="Test Todo", completed=False)]
        
        # Act
        result = get_all()
        
        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].title, "Test Todo")
    
    @patch('app.service.todo_service.get_all')
    def test_get_all_empty(self, mock_get_all):
        # Arrange
        mock_get_all.return_value = []
        
        # Act
        result = get_all()
        
        # Assert
        self.assertEqual(len(result), 0)

    @patch('app.service.todo_service.get_by_id')
    def test_get_by_id_success(self, mock_get_by_id):
        # Arrange
        mock_get_by_id.return_value = Todo(id=1, title="Test Todo", completed=False)
        
        # Act
        result = get_by_id(1)
        
        # Assert
        self.assertEqual(result.id, 1)
        self.assertEqual(result.title, "Test Todo")
    
    @patch('app.service.todo_service.get_by_id')
    def test_get_by_id_not_found(self, mock_get_by_id):
        # Arrange
        mock_get_by_id.side_effect = ValueError("Todo not found")
        
        # Act & Assert
        with self.assertRaises(HTTPException):
            get_by_id(999)

    @patch('app.service.todo_service.create')
    def test_create_success(self, mock_create):
        # Arrange
        todo_create = TodoCreate(title="New Todo", completed=False)
        new_todo = Todo(id=1, **todo_create.model_dump())
        mock_create.return_value = new_todo
        
        # Act
        result = create(todo_create)
        
        # Assert
        self.assertEqual(result.id, 1)
        self.assertEqual(result.title, "New Todo")

    @patch('app.service.todo_service.update_by_id')
    def test_update_by_id_success(self, mock_update_by_id):
        # Arrange
        todo_create = TodoCreate(title="Updated Todo", completed=True)
        updated_todo = Todo(id=1, **todo_create.model_dump())
        mock_update_by_id.return_value = updated_todo
        
        # Act
        result = update_by_id(1, todo_create)
        
        # Assert
        self.assertEqual(result.id, 1)
        self.assertEqual(result.title, "Updated Todo")
    
    @patch('app.service.todo_service.update_by_id')
    def test_update_by_id_not_found(self, mock_update_by_id):
        # Arrange
        todo_create = TodoCreate(title="Updated Todo", completed=True)
        mock_update_by_id.side_effect = ValueError("Todo not found")
        
        # Act & Assert
        with self.assertRaises(HTTPException):
            update_by_id(999, todo_create)

    @patch('app.service.todo_service.delete_by_id')
    def test_delete_by_id_success(self, mock_delete_by_id):
        # Arrange
        mock_delete_by_id.return_value = True
        
        # Act
        delete_by_id(1)
        
        # Assert
        mock_delete_by_id.assert_called_once_with(1)
    
    @patch('app.service.todo_service.delete_by_id')
    def test_delete_by_id_not_found(self, mock_delete_by_id):
        # Arrange
        mock_delete_by_id.side_effect = ValueError("Todo not found")
        
        # Act & Assert
        with self.assertRaises(HTTPException):
            delete_by_id(999)

if __name__ == '__main__':
    unittest.main()
