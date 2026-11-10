# 1. Zaloguj się do Azure
az login

# Jeśli logowanie zawiesza się w przeglądarce:
# az login --use-device-code

# 2. Ustaw parametry
RG="sages-szkolenie-przemek"
APP="sagesszkolenieprzemekasp"

# 3. Sprawdź aktywną subskrypcję
az account show --output table

<!--
# 4. Utwórz ZIP z zawartości folderu publish
cd bin
cd Publish
zip -r ../app.zip .
cd .. 
-->

# 5. Wdróż aplikację do istniejącej Azure Web App
az webapp deploy \
  --resource-group "$RG" \
  --name "$APP" \
  --src-path ./app.zip \
  --type zip

# 6. Otwórz aplikację w przeglądarce (macOS)
open "https://${APP}.azurewebsites.net"