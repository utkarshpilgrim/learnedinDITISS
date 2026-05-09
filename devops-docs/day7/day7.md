# Automation

- Alpine is the smllest linux, hardly around 8MB. Go to *hub.docker.com* and you'll find it. 

- Try to create the a container using alpine.
```
docker container run --name alpine -itd alpine
```

- Docker images can be huge, therefore use the alpine version of images, similarly for python you can use the alpine, named by python:3.9.21-alpine.

- Write the dockerfile for the catalog image and you'll find that the image for docker is going to be very less. 

```bash
FROM python:3.9.21-alpine
WORKDIR /src
COPY . .
RUN pip3 insall flask
EXPOSE 4000
CMD ["python", "server.py"]
```

- Now create the 

```bash
FROM node:alpine3.21
WORKDIR /app
COPY . .
RUN npm insall express
EXPOSE 4000
CMD ["node", "server.js"]
```

- Now create the image.

```
# creating the image manually
docker image build -t catalog_service .

# create container
docker container run --name catalog-service -itd -p 4000:4000 catalog_service
```

- Now, once there is a change in the file, you will require to drop the container, then remove the image, then create a new image, hence, you need to do something, for that. We use **Docker Compose**. We are going to use the yaml.

- Create docker-compose.yaml file. Remember these folders should be inside the folder only whre you've create user-serivce and catalog-service. 

```Dockerfile 
services:
    catalog-service:
    build: ./catalog-service/

    ports:
        - 4000:4000
    
    user-service:
        build: ./user-service/

    ports:
        - 4001:4001
```

*What is Docker Compose?* It is used to create the file that is used for the creation of the microservices at once. 

```
# 
docker compose ls

# build the image
docker compose build

# create the container for all microsrevices
docker compose up -d 

# remove the containers
docker compose down

# remove the images as well
docker compose down -rmi all
```

Remember that you don't have to explicilty run the build command in compose, if the image is yet to be build, `docker compose up -d` will do it, making life pretty easy. We can also see that when you try to ping multipl microservices within the container, they are able to identify each other.

You can also connect mysql with the databse. 

```bash
# Dockerfile

FROM mysql
ENV MYSQL_ROOT_PAAWORD
ENV MYSQL_DATABASE
COPY db_schema.sql /docker-entrypoint--initdb.d
EPOSE 3306
```

Add another service that will represent and will deploy the mysql service. 

```
db:
    build: ./db-service.

volumes:
```

```bash
FROM python:3.9.21-alpine
WORKDIR /src
COPY . .
RUN pip3 insall flask mysql-connector
EXPOSE 4000
CMD ["python", "server.py"]
```

- But is does have a disadvantage, docker compose connot run with the docker swarm. 

- In order to do that, you need to start with Docker stack. Docker stack is similr to socker compose, which is able to integrate with docker swarm. 

# Pod 

The concept is simple. WHen you are in kubernetes, you are to trip the backend and frontend together, as this solves a crucial problem, we don't have to create multiple instances for the load balancing of the frontend and backend. Instead the concept of pod is simple, pod is a group of containers 

Any object can be created using the following structure. 

1. **`apiVersion`**: v1 (simple objects) and apps/v1 (for higher objects)

2. **`kind`**: kind of object to be created

3. **`metadata`**: data about data

4. **`specs`**: specification of object

Lets take an example for the pod.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod1
  labels:
    type: app
spec:
  containers:
    - name: mycontainer
      image: httpd
```