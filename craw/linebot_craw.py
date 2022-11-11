#linebot 結合網路爬蟲
'''
使用網路爬蟲爬取 ifoodie 的餐廳：透過輸入關鍵字來爬取相關餐廳，以下範例爬取該搜尋介面的前五筆食譜，並解析其 HTML 找到餐廳名稱、評價、地址、網址等資訊。
縮短網址：此功能是因應後續要將這個 function 套用進 Line Chatbot 中的 Carousel template，而在此 template 中有限制字元的數量，
因此在此增加縮短網址的功能以避免發生 error 無法順利產生 line Chatbot 的滑動視窗。
'''
'''
step1
linefoodbot 下建立一個 scraper.py ，放入程式碼
'''
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
 
 
# 美食抽象類別
class Food(ABC):
 
    def __init__(self, area):
        self.area = area  # 地區
 
    @abstractmethod
    def scrape(self):
        pass
 
 
# 愛食記爬蟲
class IFoodie(Food):
 
    def scrape(self):
        response = requests.get(
            "https://ifoodie.tw/explore/" + self.area +
            "/list?sortby=rating&opening=true")
        
        soup = BeautifulSoup(response.content, "html.parser")
         # 爬取前五筆餐廳卡片資料
        cards = soup.find_all(
            'div', {'class': 'jsx-3292609844 restaurant-info'}, limit=5)
 
        content = ""
        for card in cards:
 
            title = card.find(  # 餐廳名稱
                "a", {"class": "jsx-3292609844 title-text"}).getText()
 
            stars = card.find(  # 餐廳評價
                "div", {"class": "jsx-1207467136 text"}).getText()
 
            address = card.find(  # 餐廳地址
                "div", {"class": "jsx-3292609844 address-row"}).getText()
 
 
            #將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
            content += f"{title} \n{stars}顆星 \n{address} \n\n"
 
        return content
