in terminal

#Django專案設定完成後，接下來就可以進行部署的動作。首先，利用以下的指令建立本地端的Git Repository，
如果LINE Bot專案在開發的過程中已經有使用Git進行版本控制的話，這個步驟可以省略。

git init


本地端的Git Repository建立完成後，利用以下四個指令，將LINE Bot專案的程式碼推送(Push)到Heroku雲端平台

$ git add .  #加入所有變更的程式碼檔案到本地端Git Repository
$ git commit -m "your_message"  #儲存到硬碟中
$ heroku git:remote -a foodielinebot000  #將Heroku雲端平台的Git Repository切換到LINE Bot的應用程式
$ git push heroku master  #推送到Heroku雲端平台的LINE Bot應用程式Git Repository

每當程式碼有修改，要部署到Heroku雲端平台時，這四個指令都需要執行。


LINE Bot Webhook URL設定
部署完成，前往LINE Developers，選擇「使用LINE帳號登入」後，點擊FoodLinebot，在Messaging API頁籤中，
Webhook URL的地方，填入Heroku雲端平台賦予的HTTPS網址，來連接LINE Bot應用程式
<img width="735" alt="截圖 2022-11-17 上午9 27 07" src="https://user-images.githubusercontent.com/102644365/202331358-e564df39-6f03-458f-bbe2-3fde0457029f.png">


執行結果
