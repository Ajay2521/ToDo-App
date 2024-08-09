import React from 'react';
import Checkbox from '@mui/material/Checkbox';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';

function TodoItem({ todo, toggleTodo, deleteTodo }) {
  return (
    <li style={{ display: 'flex', alignItems: 'center', marginBottom: '8px' }}>
      <Checkbox
        checked={todo.completed}
        onChange={() => toggleTodo(todo.id)}
      />
      <span
        style={{
          flex: '1',
          padding: '8px',
          textDecoration: todo.completed ? 'line-through' : 'none'
        }}
      >
        {todo.title}
      </span>
      <IconButton
        onClick={() => deleteTodo(todo.id)}
        color="error"
      >
        <DeleteIcon />
      </IconButton>
    </li>
  );
}

export default TodoItem;