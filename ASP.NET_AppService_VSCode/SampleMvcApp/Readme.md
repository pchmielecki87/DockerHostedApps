Source: https://learn.microsoft.com/en-us/aspnet/core/tutorials/publish-to-azure-webapp-using-vscode?view=aspnetcore-8.0

`dotnet new mvc -o MyMVCapp`
`code -r MyMVCapp`

`dotnet dev-certs https --trust`

`dotnet run`

`dotnet publish -c Release -o ./bin/Publish`

Right click the bin\Publish folder and select Deploy to Web App... and follow the prompts.
