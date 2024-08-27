# Python Flask Microservices

## Prapare svc1 Users

### Prerequisites svc1

Use venv:
`python3 -m venv svc1-venv`
`source svc1-venv/bin/activate`

Install requirements:
`pip install -r requirements.txt`
Ensure that proper versions of requirements are in place

### Prepare Docker env svc1

Navigate to svc1 folder
`docker build -t p3-microservice-user-service .`
`docker run -d -p 5011:5011 --name p3-microservice-user-service p3-microservice-user-service`

### Verify svc1

`http://127.0.0.1:5011/users`
`curl http://127.0.0.1:5011/users`
`docker logs p3-microservice-user-service`

## Prapare svc2 Products

### Prerequisites svc2

Use venv:
`python3 -m venv svc2-venv`
`source svc2-venv/bin/activate`

Install requirements:
`pip install -r requirements.txt`
Ensure that proper versions of requirements are in place

### Prepare Docker env svc2

Navigate to svc2 folder
`docker build -t p3-microservice-product-service .`
`docker run -d -p 5012:5012 --name p3-microservice-product-service p3-microservice-product-service`

### Verify svc2

`http://127.0.0.1:5012/products`
`curl http://127.0.0.1:5012/products`
`docker logs p3-microservice-product-service`

## Prapare svc3 Orders

### Prerequisites svc3

Use venv:
`python3 -m venv svc3-venv`
`source svc3-venv/bin/activate`

Install requirements:
`pip install -r requirements.txt`
Ensure that proper versions of requirements are in place

### Prepare Docker env svc3

Navigate to svc3 folder
`docker build -t p3-microservice-order-service .`
`docker run -d -p 5013:5013 --name p3-microservice-order-service p3-microservice-order-service`

### Verify svc3

`http://127.0.0.1:5013/orders`
`curl http://127.0.0.1:5013/orders`
`docker logs p3-microservice-order-service`

## Overall verify

Access the UserService at `http://localhost:5011/users`.
Access the ProductService at `http://localhost:5012/products`.
Create an order in OrderService using `POST /orders` with a JSON body like `{"user_id": 1, "product_id": 1}`.

## Docker Compose to expose services

Stop services
`docker stop p3-microservice-users-service`
`docker stop p3-microservice-products-service`
`docker stop p3-microservice-order-service`

Run Docker-Compose
`docker-compose up`
