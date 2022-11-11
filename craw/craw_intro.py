$ pip install requests
$ pip install beautifulsoup4
'''
2xx：成功獲取資料，例如「200」代表「OK」
4xx：用戶端錯誤，例如「404」代表「找不到」
5xx：伺服器故障，例如「502」代表「閘道故障」
'''

#幾個比較重要的函式

# html 是 HTML 格式的字串，我們要將他轉換成 Python 的物件才可以繼續做處理。
BeautifulSoup(html, 'html.parser')

#為了找出標籤為「tag」的所有元素。若參數「attr」存在（line 2 所示），則要找出標籤為「tag」且屬性也符合「attr」要求的所有元素。
BeautifulSoup.find_all(tag)
BeautifulSoup.find_all(tag, attr)

#找出第一個遇到標籤為「tag」的內容。
tag.contents

#找出第一個遇到標籤為「tag」所對應的標籤名稱
tag.name

#會找出第一個遇到標籤為「tag」且屬性為「attr」的值。
tag['attr']
