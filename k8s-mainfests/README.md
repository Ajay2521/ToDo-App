# Steps to deploy the application in kubernetes

## 1. push images to docker hub steps:

Push the images to your respective dockerhub public repositories

```
cd ToDo-App/

docker build -t todo-app:latest ./todo
docker tag todo-app:latest naveenmsd007/todo-app:v1 
docker push naveenmsd007/todo-app:v1


docker build -t todo-ui:latest ./react-app
docker tag todo-ui:latest naveenmsd007/todo-ui:v1 
docker push naveenmsd007/todo-ui:v1

```

## 2. create the yaml mainfests

Create the front-end and back-end microservice

```
kubectl apply -f front-end.yaml
kubectl apply -f back-end.yaml

```

## 3. create the port forward to access outside the cluster

```
# Forward backend service to localhost
kubectl port-forward service/todo-app-service 8000:8000

# Forward frontend service to localhost
kubectl port-forward service/todo-ui-service 3000:3000
```
