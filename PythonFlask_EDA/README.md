# Python Flask EDA

## Prapare app

Use venv:
`python3 -m venv flask-eda`
`source flask-eda/bin/activate`

`pip install requirements.txt`
Ensure that proper versions of requirements are in place

## Prepare Docker env

`docker-compose up --build`

## Verify

`consumer_service_1:5021`
`consumer_service_2:5022`
`producer_service:5023`

`http://localhost:6000`
`curl http://localhost:6000`


RABBIT http://localhost:15672


