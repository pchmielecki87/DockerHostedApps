# Python Django

## Prapare app

Ensure that proper versions of requirements are in place

## Prepare Docker env

`docker build -t django-docker-app .`
`docker run -d -p 8000:8000 --name django-container django-docker-app`

## Verify

`http://localhost:8000`