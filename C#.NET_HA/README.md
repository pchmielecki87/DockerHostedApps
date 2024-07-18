# Microsoft Learn for .NET Cloud Native Development

This repo contains the sample code for all the exercises in the [cloud native learning path for .NET](https://learn.microsoft.com/training/paths/create-microservices-with-dotnet/).

- Select **Code**.
- Select the **Codespaces** tab `<img src="codespace-with-options.png" width="500" alt="A screenshot showing the New with options menu."/>`
- Select **...** (Codespace respository configuration), then select **+ New with options**.
- Select the devcontainer for the module you want `<img src="choose-dev-container.png" width="800" alt="A screenshot showing the devcontainer." />`

## Build and test

### Build app

`cd dotnet-resiliency`
`dotnet publish /p:PublishProfile=DefaultContainer`
`docker compose up`
`http://localhost:32000/products`

### Add HA

`cd Store`
`dotnet add package Microsoft.Extensions.Http.Resilience`
`using Microsoft.Extensions.Http.Resilience;`
`.AddStandardResilienceHandler()`
