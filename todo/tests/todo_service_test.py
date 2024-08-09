import unittest
from unittest.mock import patch, MagicMock
from app.service.todo_service import *
from app.models.todo import Todo, TodoCreate

class TestTodoService(unittest.TestCase):

    @patch('app.repo.todo_repo.get_all')
    def test_get_all(self, mock_get_all):
        # Setup
        mock_get_all.return_value = [
            Todo(id=1, title="Test Todo 1", completed=False),
            Todo(id=2, title="Test Todo 2", completed=True)
        ]

        # Action
        todos = get_all()

        # Assert
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].id, 1)
        self.assertEqual(todos[1].title, "Test Todo 2")

    @patch('app.repo.todo_repo.get_by_id')
    def test_get_by_id_success(self, mock_get_by_id):
        # Setup
        mock_get_by_id.return_value = Todo(id=1, title="Test Todo", completed=False)

        # Action
        todo = get_by_id(1)

        # Assert
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test Todo")

    @patch('app.repo.todo_repo.get_by_id')
    def test_get_by_id_not_found(self, mock_get_by_id):
        # Setup
        mock_get_by_id.return_value = None

        # Action & Assert
        with self.assertRaises(ValueError) as context:
            get_by_id(999)
        self.assertEqual(str(context.exception), "Todo not found")

    @patch('app.repo.todo_repo.create')
    @patch('app.repo.todo_repo.get_all')
    def test_create(self, mock_get_all, mock_create):
        # Setup
        mock_get_all.return_value = []
        mock_create.return_value = None

        todo_create = TodoCreate(title="New Todo", completed=False)

        # Action
        todo = create(todo_create)

        # Assert
        self.assertEqual(todo.title, "New Todo")
        self.assertEqual(todo.completed, False)
        self.assertEqual(todo.id, 1)  # Assuming this is the first todo created

    @patch('app.repo.todo_repo.update_by_id')
    @patch('app.repo.todo_repo.get_all')
    def test_update_by_id_success(self, mock_get_all, mock_update_by_id):
        # Setup
        mock_get_all.return_value = [Todo(id=1, title="Old Todo", completed=False)]
        mock_update_by_id.return_value = True

        todo_update = TodoCreate(title="Updated Todo", completed=True)

        # Action
        updated_todo = update_by_id(1, todo_update)

        # Assert
        self.assertEqual(updated_todo.id, 1)
        self.assertEqual(updated_todo.title, "Updated Todo")
        self.assertEqual(updated_todo.completed, True)

    @patch('app.repo.todo_repo.update_by_id')
    def test_update_by_id_not_found(self, mock_update_by_id):
        # Setup
        mock_update_by_id.return_value = False

        todo_update = TodoCreate(title="Updated Todo", completed=True)

        # Action & Assert
        with self.assertRaises(ValueError) as context:
            update_by_id(999, todo_update)
        self.assertEqual(str(context.exception), "Todo not found")

    @patch('app.repo.todo_repo.delete_by_id')
    def test_delete_by_id_success(self, mock_delete_by_id):
        # Setup
        mock_delete_by_id.return_value = True

        # Action
        delete_by_id(1)

        # Assert
        mock_delete_by_id.assert_called_once_with(1)

    @patch('app.repo.todo_repo.delete_by_id')
    def test_delete_by_id_not_found(self, mock_delete_by_id):
        # Setup
        mock_delete_by_id.return_value = False

        # Action & Assert
        with self.assertRaises(ValueError) as context:
            delete_by_id(999)
        self.assertEqual(str(context.exception), "Todo not found")

if __name__ == '__main__':
    unittest.main()