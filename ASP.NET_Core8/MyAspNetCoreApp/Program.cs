var builder = WebApplication.CreateBuilder(args);
builder.WebHost.ConfigureKestrel(serverOptions =>
{
    serverOptions.ListenAnyIP(80); // Listen on port 80 on any IP address
});
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();
