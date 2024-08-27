# Python Flask SOA

## Prapare app

Use venv:
`python3 -m venv flask-soa`
`source flask-soa/bin/activate`

`pip install -r requirements.txt`
Ensure that proper versions of requirements are in place

## Prepare Docker env

`docker build -t flask-docker-app .`
`docker run -d -p 6000:6000 --name flask-container flask-docker-app`

## Verify

`http://localhost:6000`
`curl http://localhost:6000`
