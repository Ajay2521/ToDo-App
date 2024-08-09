# Use an official Node.js runtime as a parent image
FROM node:18 AS build

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of the application files
COPY . .

# Build the React application
RUN npm run build

# Install `serve` globally to serve the React app
RUN npm install -g serve

# Expose port 3000 to the outside world
EXPOSE 3000

# Serve the React application using `serve`
CMD ["serve", "-s", "build", "-l", "3000"]