# linechatbot-crawing


$ pip install django
$ pip install line-bot-sdk
$ pip install requests

# Chatbot 專案


在 vscode terminnal 打上下列文字，建立 Django 專案，以 mylinebot 為例

django-admin startproject mylinebot  #在目前的資料夾下建立專案

執行完後，可以看到django-admin套件管理工具在Django專案中建立了一個基本的網站架構，包含了專案主程式資料夾(potrip)及manage.py檔
<img width="175" alt="截圖 2022-11-11 上午8 45 15" src="https://user-images.githubusercontent.com/102644365/201236702-b60aa4e6-c779-4b27-b8bd-adc578f90751.png">

進入到 mylinebot 檔案夾
cd mylinebot

建立Django應用程式 程式名稱 foodlinebot

python manage.py startapp foodlinebot

mylinebot 是專案主程式
foodlinebot 是應用程式

<img width="156" alt="截圖 2022-11-11 上午8 59 41" src="https://user-images.githubusercontent.com/102644365/201237728-70a9f3ed-5474-4677-82bb-81fe47214041.png">

#新增憑證



開啟專案，我們在 mylinebot/settings.py 裡增加上Basic Settings 裡的 Channel Secret 和 Messaging API 裡的 Channel access token 憑證
INE_CHANNEL_ACCESS_TOKEN = 'Messaging API > Channel access token'
LINE_CHANNEL_SECRET = 'Basic settings > Channel secret'

然後在同一個 settings.py 檔裡面的 INSTALLED_APPS 加上剛剛所建立的 Django 應用程式，新增APP名稱

'foodlinebot.apps.FoodlinebotConfig',
