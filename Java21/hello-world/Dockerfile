FROM tomcat:11.0-jdk21

# Remove default Tomcat applications
RUN rm -rf /usr/local/tomcat/webapps/*

# Copy our WAR file to the webapps directory
COPY target/hello-world-java21.war /usr/local/tomcat/webapps/ROOT.war

# Expose the default Tomcat port
EXPOSE 8080

# Start Tomcat
CMD ["catalina.sh", "run"]
