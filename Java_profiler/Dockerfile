FROM openjdk:8-alpine
COPY HelloWorld.java HelloWorld.java
COPY MANIFEST.MF MANIFEST.MF
RUN javac HelloWorld.java
RUN jar cfmv HelloWorld.jar MANIFEST.MF HelloWorld.class
RUN ls -lah
EXPOSE 9010
CMD java \
    -Dcom.sun.management.jmxremote=true \
    -Dcom.sun.management.jmxremote.local.only=false \
    -Dcom.sun.management.jmxremote.authenticate=false \
    -Dcom.sun.management.jmxremote.ssl=false \
    -Djava.rmi.server.hostname=localhost \
    -Dcom.sun.management.jmxremote.port=9010 \
    -Dcom.sun.management.jmxremote.rmi.port=9010 \
    -jar HelloWorld.jar