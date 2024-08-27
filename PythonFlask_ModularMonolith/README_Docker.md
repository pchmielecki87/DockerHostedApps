# General

Works locally, Docker need to be fixed

## Prepare Docker env

`docker build -t p3mm2 . --no-cache`
`docker run -d -p 5001:5000 --name p3mm2 py3modularmono2`

## Verify

`http://localhost:5001`
`curl http://localhost:5001`
`docker logs py3modularmono2`
