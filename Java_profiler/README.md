Based on example [link](https://technicaldifficulties.io/2017/12/19/connecting-visualvm-to-a-local-docker-container-from-scratch/)

docker build -t helloworld .   
docker run -d -p 9010:9010 --name helloworld helloworld
docker logs helloworld
(optionally) docker rm <id>