#安裝Git

Git是一個版本控制系統(Version Control System)，除了可以協助開發人員進行程式碼的版本控制外，在部署時也能夠將程式碼推送(Push)到Heroku雲端平台的Git Repository。
前往Git官網的下載頁面，依照作業系統進行安裝
安裝完成後，開啟命令提示字元視窗，輸入以下指令

$ git --version

如果有顯示版本號，即代表Git安裝成功

#安裝gunicorn
將LINE Bot部署到Heroku雲端平台時，在HTTP請求(Request)的處理上，就需要使用WSGI(Web Server Gateway Interface)介面，
來負責網頁伺服器(Heroku雲端平台)與網頁應用程式(LINE Bot)之間的溝通，而Python的gunicorn伺服器就是扮演這樣的角色

$ pip install gunicorn

#安裝Heroku CLI
Heroku是一個平台即服務(PaaS)的雲端平台，支援多種程式語言，開發人員能夠直接利用Git快速部署應用程式，並且提供CLI(Command-Line Interface)，
可以透過指令來進行操作，提升部署的效率。
註冊並且登入成功後，在左下角的地方可以看到「The Heroku CLI」點擊後，往下就可以看到安裝的畫面
依據作業系統進行安裝即可。完成後，利用Visual Studio Code開啟LINE Bot專案，在Terminal視窗中，透過以下的Heroku CLI指令進行登入：

$ heroku login
$ heroku create foodielinebot000
<img width="890" alt="截圖 2022-11-17 上午9 40 28" src="https://user-images.githubusercontent.com/102644365/202333034-7fce23a1-5a6d-45a0-9edb-a7471d44ed8f.png">

Heroku雲端平台就會為這個應用程式，產生一組HTTPS的網址及Git Repository，之後，就是要將LINE Bot專案的程式碼推送到這個Git Repository來進行部署。
*<img width="526" alt="截圖 2022-11-17 上午9 41 48" src="https://user-images.githubusercontent.com/102644365/202333189-95487b05-0ad1-443d-9b5e-42516e0d8c4b.png">
換個名字就可以了喔！

#LINE Bot專案設定
<img width="224" alt="截圖 2022-11-17 上午9 43 16" src="https://user-images.githubusercontent.com/102644365/202333391-34a30d1d-b03c-4c71-ab45-e05ce01a6377.png">

建立Procfile檔案
用來告訴Heroku雲端平台，利用gunicorn伺服器，執行Django專案中的wsgi(web server gateway interface)檔案，來進行溝通。
在專案最外層新增一個Procfile檔案，並且輸入以下的範例設定，特別注意，在新增Procfile檔案時，不需要輸入副檔名。
web: gunicorn mylinebot.wsgi
目前LINE Bot專案的架構如下圖：
<img width="224" alt="截圖 2022-11-17 上午9 45 06" src="https://user-images.githubusercontent.com/102644365/202333665-8727b17e-d477-4bbd-972a-1de63267805d.png">

*注意 Procfile 的 P  一定要大寫 

建立requirements.txt檔案
在部署的過程中，用來告訴Heroku雲端平台有哪些套件需要進行安裝，可以透過以下的指令來產生：
$ pip freeze > requirements.txt
*anaconda 環境下會變成全部都是 @file，可以用

pip list --format=freeze > requirements.txt

<img width="213" alt="截圖 2022-11-17 上午9 52 07" src="https://user-images.githubusercontent.com/102644365/202334518-4c5b0bf3-bc46-470b-a038-6808369efeae.png">

建立STATIC資料夾
由於Django為網頁框架，而網頁通常都會有靜態檔案，像是Javascript、CSS及Image(圖片)檔等，所以Heroku雲端平台會讀取專案中的static資料夾，
如果沒有建立的話，在部署時會發生錯誤
由於LINE Bot不會有上面所提到的靜態檔案，所以資料夾中保持空白即可。接著，開啟settings.py檔案，新增這個static資料夾的路徑設定

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

設定ALLOWED_HOSTS
開啟settings.py檔案，在ALLOWED_HOSTS的地方，加入Heroku雲端平台所產生的應用程式網址，來允許這個網址的請求(Request)
ALLOWED_HOSTS = [
    'foodielinebot000.herokuapp.com'
]


