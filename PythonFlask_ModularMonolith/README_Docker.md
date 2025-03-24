# General

Works locally, as well as in Docker.

Use venv:
`python3 -m venv mono-venv`
`source mono-venv/bin/activate`

## Prepare Docker env

`docker build -t p3mm . --no-cache`
`docker run -d -p 5001:5000 --name py3modularmono p3mm`

## Verify

`http://localhost:5001`
`curl http://localhost:5001`
`docker logs py3modularmono`
