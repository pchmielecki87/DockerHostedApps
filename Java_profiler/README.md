Based on example [link](https://technicaldifficulties.io/2017/12/19/connecting-visualvm-to-a-local-docker-container-from-scratch/)

# Install Java
brew install openjdk
export JAVA_HOME="/usr/local/opt/openjdk/libexec/openjdk.jdk/Contents/Home"
sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
java -version
javac -version

# Run VisualVM 
(for Intel MacBook) 
cd /Applications/VisualVM.app/Contents/Resources/visualvm/bin 
./visualvm --jdkhome /opt/homebrew/opt/openjdk/libexec/openjdk.jdk 

# Run Java app
docker build -t helloworld .   
docker run -d -p 9010:9010 --name helloworld helloworld
docker logs helloworld
(optionally) docker rm <id>