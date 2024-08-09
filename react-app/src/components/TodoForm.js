import React, { useState } from 'react';
import TodoFormContent from './TodoFormContent';

function TodoForm({ addTodo }) {
  const [title, setTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim()) return;
    addTodo(title);
    setTitle('');
  };

  return (
    <TodoFormContent
      title={title}
      setTitle={setTitle}
      handleSubmit={handleSubmit}
    />
  );
}

export default TodoForm;