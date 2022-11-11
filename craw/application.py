import requests
from bs4 import BeautifulSoup
response = requests.get(https://cookpad.com/tw)
print(response.status_code)
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

# 403，代表的意思是「伺服器成功解析請求但是客戶端沒有存取該資源的權限」，也就是我們被發現是機器人，然後被擋下來了
# 使用假header
user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)'
headers = {'User-Agent': user_agent}
response = requests.get('https://cookpad.com/tw', headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

#假 header 其實也有套件可以使用！我們可以使用一個叫 fake-useragent 的套件來自動產生假的 header
$ pip install fake-useragent

from fake_useragent import UserAgent
ua = UserAgent()
# Safari 的 UA
user_agent = ua.safari
# IE 的 UA
user_agent = ua.ie
# Chrome 的 UA
user_agent = ua.chrome
# 隨機產生的 UA
user_agent = ua.random
