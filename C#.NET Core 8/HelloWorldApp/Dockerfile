# Use the official IIS base image
FROM mcr.microsoft.com/dotnet/framework/aspnet:4.8-windowsservercore-ltsc2019

# Set environment variables
ENV ASPNETCORE_URLS=http://+:80
ENV ASPNETCORE_ENVIRONMENT=Production

# Create a directory in the container
WORKDIR /inetpub/wwwroot

# Copy the published output from the host to the container
COPY out/ .

# Expose port 80
EXPOSE 80
