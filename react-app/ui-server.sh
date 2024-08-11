#!/bin/bash

# Build the Docker image
build(){
    echo -e "🚀 Building the Docker image...\n"
    docker build -t todo-ui .
    echo -e "✅ Docker image built successfully!\n"
}


# Start the server in the foreground
start_container(){
    echo -e "🔄 Starting the todo-ui server...\n"
    docker run --name todo-ui-server -p 3000:3000 todo-ui
    echo -e "🟢 Server is running on http://localhost:3000 \n"
}


# Cleanup on stop
stop_container(){
    echo -e "🧹 Cleaning up resources...\n"
    docker rm todo-ui-server --force
    echo -e "❌ Removed the running container.\n"
}

# remove image
clean_up_image(){
    docker rmi todo-ui
    echo -e "🗑️ Removed the Docker image.\n"
}

arg=$1
if [[ $arg == "--build" ]]; then
    build
elif [[ $arg == "--start" ]]; then
    start_container
elif [[ $arg == "--stop" ]]; then
    stop_container
elif [[ $arg == "--clean" ]]; then
    stop_container
    clean_up_image
elif [[ $arg == "--all" ]]; then
    build
    start_container
    stop_container
    clean_up_image
else
    echo "Usage:"
    echo "./ui-server.sh --build:      Build the Docker image"
    echo "./ui-server.sh --start:      Start the server"
    echo "./ui-server.sh --stop:       Stop the server"
    echo "./ui-server.sh --clean:      Stop the server and clean up the old image"
    echo "./ui-server.sh --all:        Build, start, and then stop the server"
fi