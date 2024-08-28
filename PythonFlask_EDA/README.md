# Python Flask EDA

## Prapare app

Use venv:
`python3 -m venv flask-eda`
`source flask-eda/bin/activate`

`pip install requirements.txt`
Ensure that proper versions of requirements are in place

## Prepare Docker env

`docker-compose up --build`
or
`COMPOSE_LOG_LEVEL=DEBUG docker-compose up --build`

Use `ctrl+c` to stop.

## Verify

RabbitMQ service `http://localhost:15672`. The user is `guest` and password the same.

Navigate to EDA folder and
`docker-compose logs event-driven-app-consumer_service_1`
and similarly to other services.

NOTE:
`consumer_service_1:5021`
`consumer_service_2:5022`
`producer_service:5023`
