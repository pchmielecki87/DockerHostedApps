# Java app

Tomcat 11
Java 21

## Build Java app

`mvn clean package`

## Host on Docker

`docker rm hello-world-java21-container`
`docker build -t hello-world-java21 .`
`docker run -d -p 8080:8080 --name hello-world-java21-container hello-world-java21`

### Stop Docker

`docker stop hello-world-java21-container`

## Verify Java app

`docker logs hello-world-java22-container`
`docker exec -it hello-world-java22-container /bin/bash`

`cat /usr/local/tomcat/logs/`
    `catalina.2024-xx-xx.log`
    `localhost.2024-xx-xx.log`
    `localhost_access_log.2024-xx-xx.txt`
