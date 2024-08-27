# Python Django

## Prapare app

Use venv:
`python3 -m venv soa1-venv`
`source soa1-venv/bin/activate`

`pip install -r requirements.txt`

Ensure that proper versions of requirements are in place

## Prepare Docker env

Navigate to SOA1 UserService folder.
`docker build -t p3soau .`
`docker run -d -p 5002:5002 --name py3soauserservice p3soau`

## Verify

`http://127.0.0.1:5002/users/1`
`curl http://127.0.0.1:5002/users/1`
`docker logs py3soauserservice`
