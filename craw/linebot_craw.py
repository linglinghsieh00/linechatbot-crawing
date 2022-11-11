#linebot 結合網路爬蟲
'''
使用網路爬蟲爬取 ifoodie 的餐廳：透過輸入關鍵字來爬取相關餐廳，以下範例爬取該搜尋介面的前五筆食譜，並解析其 HTML 找到餐廳名稱、評價、地址、網址等資訊。
縮短網址：此功能是因應後續要將這個 function 套用進 Line Chatbot 中的 Carousel template，而在此 template 中有限制字元的數量，
因此在此增加縮短網址的功能以避免發生 error 無法順利產生 line Chatbot 的滑動視窗。
''
