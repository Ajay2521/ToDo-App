import React from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

function TodoFormContent({ title, setTitle, handleSubmit }) {
  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: '20px', display: 'flex', alignItems: 'center' }}>
      <TextField
        label="Add new todo"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        variant="outlined"
        size="small"
        style={{ flex: '1', marginRight: '8px' }}
      />
      <Button
        type="submit"
        variant="contained"
        color="primary"
        disableElevation
      >
        Add
      </Button>
    </form>
  );
}

export default TodoFormContent;