列出我在部署遇到的問題
1. requitements.txt 
1.1
<img width="623" alt="截圖 2022-11-14 下午3 28 01" src="https://user-images.githubusercontent.com/102644365/202337032-1d7a7826-8e63-4121-86b9-9c19e9a660b1.png">

<img width="623" alt="截圖 2022-11-14 下午3 28 36" src="https://user-images.githubusercontent.com/102644365/202336611-8b932ae6-e8bd-4d19-bbb7-a3d4803d498e.png">
<img width="898" alt="截圖 2022-11-14 上午10 57 35" src="https://user-images.githubusercontent.com/102644365/202335423-dd676766-2c9c-4986-9bbc-3c40a40bb074.png">
anaconda 無法使用
$ pip freeze > requirements.txt
改用
$ pip list --format=freeze > requirements.txt

1.2
<img width="759" alt="截圖 2022-11-16 下午8 19 55" src="https://user-images.githubusercontent.com/102644365/202335910-a1e10e6b-8102-417e-a6d2-17f05a9ca1e9.png">
會有很多奇怪的安裝包出現，導致錯誤
<img width="213" alt="截圖 2022-11-17 上午10 03 07" src="https://user-images.githubusercontent.com/102644365/202336027-9baae423-d49b-4a2c-a4eb-b35f4e6a5cf6.png">
慢慢刪檔案吧！這我也還沒找到解決方法

2.heroku 創建 app 時
<img width="569" alt="截圖 2022-11-13 下午4 52 38" src="https://user-images.githubusercontent.com/102644365/202337692-f6f96db8-045d-4d59-b700-5a830d197532.png">
把 foodielinebot 換成別的名字，我換成 foodielinebot000

3.  部署 linebot verify 遇到 503 的問題
3.1
檢查 Procfile 的 p 是不是大寫
3.2
輸入
heroku ps: scale web=1
如果出現
<img width="617" alt="截圖 2022-11-16 下午10 25 19" src="https://user-images.githubusercontent.com/102644365/202339140-90587638-b6b5-4b83-a2ec-38e4248f978c.png">
Couldn't find that process type (web).
輸入
% heroku logs --tail
<img width="754" alt="截圖 2022-11-16 下午10 25 48" src="https://user-images.githubusercontent.com/102644365/202339559-fa70e62d-7caf-4492-a7d5-54b2f58d0cf7.png">
<img width="754" alt="截圖 2022-11-16 下午10 25 48" src="https://user-images.githubusercontent.com/102644365/202339640-3ca9a183-a446-4ac2-9999-ad7889c453bf.png">
發現是 at=error code=H14 desc="No web processes running"
上網查後
<img width="402" alt="截圖 2022-11-16 下午10 25 04" src="https://user-images.githubusercontent.com/102644365/202339770-1f7dc576-5cff-4a52-bc54-4ea072376633.png">
再
$ git add .  #加入所有變更的程式碼檔案到本地端Git Repository
$ git commit -m "your_message"  #儲存到硬碟中
$ heroku git:remote -a foodielinebot  #將Heroku雲端平台的Git Repository切換到LINE Bot的應用程式
$ git push heroku master  #推送到Heroku雲端平台的LINE Bot應用程式Git Repository
就成功拉
<img width="759" alt="截圖 2022-11-16 下午9 20 08" src="https://user-images.githubusercontent.com/102644365/202340086-6934b580-d9c3-44df-ac80-0588d51d991c.png">
<img width="612" alt="截圖 2022-11-17 上午10 31 13" src="https://user-images.githubusercontent.com/102644365/202340161-b4eba015-ad3f-41b1-a471-bcb3b212d58f.png">
好感動！！！終於完成了
