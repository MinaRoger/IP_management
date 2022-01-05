#IP Management System

## Dependencies:

- Docker
    - You can download it from https://www.docker.com/get-started

- Docker Compose
    - You can install it from https://docs.docker.com/compose/install/


## Development:

### First time setup:

```
$ docker-compose build
$ docker-compose up
```

| WARNING: If you are using Windows as your operating system, make sure to set entrypoint.sh line separator conversion to LF|
| --- |


### Accessing manage.py:
```
$ docker exec -it container_id python manage.py createsuperuser
```

| NOTE : To get your container id use `$ docker ps`  |
| --- |

### Running the development server:

```
$ docker-compose up
```
###Accessing admin portal
  http://localhost:8000/admin
###Accessing endpoints documentation
  http://localhost:8000/docs  
  
##Files Structure
Django is using MVC Design Pattern where 
  - Model is the database model
  - Views is the template
  - Controller is the views

In Each module you will find this structure
```
IP_mangement
│   README.md
│      
│
└───subnet
│   │   
│   │   
│   │
│   └───migrations  (DataBase creation /updates queries)
│   │    │   migration 1
│   │    │   migration 2
│   │    │   ...
│   │
│   └─── models (Database models)
│   │    │  subnet.py
│   │    │  reserved_ip.py
│   │    │   ...
│   │
│   └── views (APIS)
│   │    │   subnet_views.py
│   │    │   reserve_ip_views.py
│   │    │   ...
│   │
│   └──services (Helper functions)
│
│
└───Dockerfile
│
│



```
##Postman Collection
https://www.getpostman.com/collections/c7d167465292e883c2ab