# Python Django

## Prapare app

Use venv:
`python3 -m venv soa2-venv`
`source soa2-venv/bin/activate`

`pip install -r requirements.txt`

Ensure that proper versions of requirements are in place

## Prepare Docker env

Navigate to SOA2 ProductService folder.
`docker build -t p3soap .`
`docker run -d -p 5003:5003 --name py3soaproductservice p3soap`

## Verify

`http://127.0.0.1:5003/products/1`
`curl http://127.0.0.1:5003/products/1`
`docker logs py3soaproductservice`
