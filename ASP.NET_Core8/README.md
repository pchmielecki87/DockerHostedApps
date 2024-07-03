# C# .NET Core 8

## Prepare app

```csharp
dotnet new web -n MyAspNetCoreApp
cd MyAspNetCoreApp
dotnet publish -c Release -o out
```

## Prepare and run Dockerfile

`docker build -t myaspnetcore8app .`
`docker run -d -p 8080:80 --name myaspnetcore8container myaspnetcore8app`
`http://localhost:8080`

## (optional) Use Docker Compose

`docker-compose up -d`

## Stop and remove container

`docker stop <container_name>`
`docker rm <container_name>`
