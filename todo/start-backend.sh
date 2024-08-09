#!/bin/bash

# Build the Docker image
echo -e "🚀 Building the Docker image...\n"

docker build -t todo-app .
echo -e "✅ Docker image built successfully!\n"

# Start the server in the foreground
echo -e "🔄 Starting the todo-app server...\n"

docker run --name todo-app-server -p 8000:8000 todo-app
echo -e "🟢 Server is running on http://localhost:8000 \n"

# Cleanup on stop
echo -e "🧹 Cleaning up resources...\n"

docker rm todo-app-server --force
echo -e "❌ Removed the running container.\n"
docker rmi todo-app
echo -e "🗑️ Removed the Docker image.\n"
