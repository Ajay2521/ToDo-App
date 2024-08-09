import unittest
from app.models.todo import Todo, TodoCreate
from app.repo.todo_repo import *

class TestTodoRepo(unittest.TestCase):
    def setUp(self):
        # Clear the in-memory storage before each test
        global todos
        todos.clear()

    def test_create_todo_success(self):
        todo = TodoCreate(title="Test Todo", completed=False)
        create(Todo(id=1, **todo.model_dump()))
        self.assertEqual(len(get_all()), 1)
        self.assertEqual(get_all()[0].title, "Test Todo")
    
    def test_get_all_todos_empty(self):
        self.assertEqual(get_all(), [])
    
    def test_get_all_todos_non_empty(self):
        todo = TodoCreate(title="Test Todo", completed=False)
        create(Todo(id=1, **todo.model_dump()))
        self.assertEqual(len(get_all()), 1)
    
    def test_get_by_id_success(self):
        todo = TodoCreate(title="Test Todo", completed=False)
        create(Todo(id=1, **todo.model_dump()))
        result = get_by_id(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Test Todo")
    
    def test_get_by_id_not_found(self):
        result = get_by_id(999)
        self.assertIsNone(result)
    
    def test_update_by_id_success(self):
        todo = TodoCreate(title="Test Todo", completed=False)
        create(Todo(id=1, **todo.model_dump()))
        updated_todo = TodoCreate(title="Updated Todo", completed=True)
        success = update_by_id(1, Todo(id=1, **updated_todo.model_dump()))
        self.assertTrue(success)
        result = get_by_id(1)
        self.assertEqual(result.title, "Updated Todo")
        self.assertTrue(result.completed)
    
    def test_update_by_id_not_found(self):
        updated_todo = TodoCreate(title="Updated Todo", completed=True)
        success = update_by_id(999, Todo(id=999, **updated_todo.model_dump()))
        self.assertFalse(success)
    
    def test_delete_by_id_success(self):
        todo = TodoCreate(title="Test Todo", completed=False)
        create(Todo(id=1, **todo.model_dump()))
        success = delete_by_id(1)
        self.assertTrue(success)
        self.assertEqual(len(get_all()), 0)
    
    def test_delete_by_id_not_found(self):
        success = delete_by_id(999)
        self.assertFalse(success)
        self.assertEqual(len(get_all()), 0)

if __name__ == '__main__':
    unittest.main()