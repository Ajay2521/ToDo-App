# Steps to deploy the application in kubernetes

## 1. Prerequesites

Install the below softwares:
- If using windows then better download wsl2 and install other softwares inside wsl2
- docker
```
https://docs.docker.com/engine/install/
```
- kubectl command line tool
```
https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
```
- k9s - termial GUI aka simiplified way to view k8s clusters 

```
https://webinstall.dev/k9s/
```
- kind - light weight k8s cluster suitable for local development and testing 
```
https://kind.sigs.k8s.io/docs/user/quick-start/
```

## 2. Create a kubernetes cluster

Create your own local kubernetes cluster for deploying our todo App.
```
kind create cluster --name=my-k8s-cluster
```

## 3. Push images to docker hub steps:

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

## 4. create the yaml mainfests

Create the front-end and back-end microservice

```
kubectl apply -f front-end.yaml
kubectl apply -f back-end.yaml

```

## 5. create the port forward to access outside the cluster

```
# Forward backend service to localhost
kubectl port-forward service/todo-app-service 8000:8000

# Forward frontend service to localhost
kubectl port-forward service/todo-ui-service 3000:3000
```
