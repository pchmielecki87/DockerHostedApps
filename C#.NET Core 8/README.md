# C# .NET Core 8

## Prepare app

```csharp
dotnet new web -n HelloWorldApp
cd HelloWorldApp
dotnet publish -c Release -o out
```

## Prepare and run Dockerfile

`docker build -t helloworldapp .`
`docker run -d -p 8080:80 --name helloworldappcontainer helloworldapp`
`http://localhost:8080`
