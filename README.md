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



#連線
Chatbot 雖然已經把主要的邏輯運算都寫好了，但是還不能執行，因為我們還沒有進行連線
在 def callback 中，會偵測到使用者是否有事件傳入（也就是有沒有使用者傳入訊息），之後就會透過 Python 迴圈去處理。
1. 不過，為了要讓使用者能夠存取到Django中的應用程式，就需要定義它的網址，所以我們要建立一個新的檔案 foodlinebot/urls.py 並加入網址設定 (見 seturl 第二個程式)
2. 之後我們要將這個 APP 網址加到專案主程式中，所以在 mylinebot/urls.py 檔案中加入網址設定（見 seturl 第二個程式)



#公開 APP 網址
ngrok 是一個可以讓內網伺服器與外界溝通的一個服務。(將 http:// 變成 https:// ) 
在官網下載 ngrok 後就可以在 terminal 上輸入
ngrok authtoken <YOUR TOKEN>
接著，就可以透過Ngrok，將本機的埠號對外公開。
Django在本機運行的埠號為8000，所以輸入以下的指令
ngrok http 8000
執行結果如下
<img width="787" alt="截圖 2022-11-11 上午10 14 47" src="https://user-images.githubusercontent.com/102644365/201247655-8b7a4db1-46d6-412f-8a64-abe475187253.png">

Forwarding 後為公開網址
localhost 是 https://localhost:8000
要特別注意的是，每次重新連接後的網址都不同，因為是隨機產生的一個對外公開的 https 網址，所以每一次重新連接，以下的東西都要重新更改一次。
我們把產生出來的一個 https 網址填入 Line Developers 的 Messageing API > Webhook settings > Webhook URL，不過還要再後面接上 Line Bot APP 的網址，記得打開 use webhook，如圖：

<img width="652" alt="截圖 2022-11-11 上午10 17 18" src="https://user-images.githubusercontent.com/102644365/201247930-f92209d6-0960-4353-9276-921697f4629e.png">

然後我們也要填入專案主程式的 setting，mylinebot/settings.py
<img width="476" alt="截圖 2022-11-11 上午10 19 52" src="https://user-images.githubusercontent.com/102644365/201248267-198a2163-61e9-4e21-9fbf-a35c83f4f547.png">


#Line Developer Setting
我們要做最後一步的設定。在 Messaging API > LINE Official Account features > Auto-reply messages > Edit

<img width="657" alt="截圖 2022-11-11 上午10 21 37" src="https://user-images.githubusercontent.com/102644365/201248467-c80ff1cc-b5cb-42e0-b15b-2974b75beda3.png">

Main settings
Response mode：我們選擇 Bot 就可以讓我們撰寫的聊天機器人自動回復
Greeting message：可以選擇加入好友後是否要先傳一個招呼訊息（也可以編輯）

Detailed settings
Auto-response：要記得把 Auto-response 關掉
Webhooks：這個選項要記得打開(Enabled)。
都設定完後，Line Channel 就能夠與 Line Bot APP 互相連結

#執行！
在 terminal 執行
python manage.py runserver

不過！！
如果更新過  foodlinebot > models.py
請先執行
python manage.py foodlinebot 
python manage.py migrate

<img width="675" alt="截圖 2022-11-11 上午10 25 41" src="https://user-images.githubusercontent.com/102644365/201249026-4430d991-5217-452b-9b15-2349afdba4cd.png">



