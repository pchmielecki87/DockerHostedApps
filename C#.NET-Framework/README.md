# ASP.NET Core 8.0

## Create ASP.NET app

`dotnet new webapp -n HelloWorldApp`
`dotnet run`

## Build Docker image and run it

`docker build -t hello-world-aspnet .`
`docker run -d -p 8080:80 --name hello-world-container hello-world-aspnet`