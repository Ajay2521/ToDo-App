import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.todo_routes import todo_router

app = FastAPI(
    title="Todo API",
    description="A simple API for managing Todo items.",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify allowed origins here
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods or specify the ones you need
    allow_headers=["*"],  # Allow all headers or specify the ones you need
)

# Include the Todo routes
app.include_router(todo_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)