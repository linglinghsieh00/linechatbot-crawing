'''
主選單建議在另一個 python 檔去撰寫執行，因為他並不是一個需要一直 call request 的東西。
rich_menu.py
'''
#step1
import requests
import json

#使用 token，我們需要 Channel access token (long-lived)

import requests
import json

LINE_CHANNEL_ACCESS_TOKEN = 'XXXXXXX'

token = LINE_CHANNEL_ACCESS_TOKEN

Authorization_token = "Bearer " + LINE_CHANNEL_ACCESS_TOKEN

headers = {"Authorization":Authorization_token, "Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "false",
    "name": "Menu",
    "chatBarText": "更多資訊",
    "areas":[
        {
          "bounds": {"x": 113, "y": 45, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "身體資訊"}
        },
        {
          "bounds": {"x": 1321, "y": 45, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "營養素"}
        },
        {
          "bounds": {"x": 113, "y": 910, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "吃"}
        },
        {
          "bounds": {"x": 1321, "y": 910, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "運動gogo"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)

'''
print 出來的值
D:\anaconda3\python.exe F:/AI/Line_Chatbot/django_chatbot/django_chatbot/rich_menu.py
{"richMenuId":"richmenu-一串數字"}
richmenu-一串數字
這是我們的 rich menu 的 ID，要記住！！
得到我們要的 ID 以後，上面 body 部分就不是重點，也只需要執行這一次。（註解掉註解掉）
'''

#step2
from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi(token)
rich_menu_id = "Rich Menu ID" # 設定成我們的 Rich Menu ID

path = "path of your image" # 主選單的照片路徑

with open(path, 'rb') as f:
    line_bot_api.set_rich_menu_image(rich_menu_id, "image/png", f)
#要注意，圖片也只要設定一次就好，要不然會出現 error

#step3
req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+rich_menu_id,headers=headers)
print(req.text)
rich_menu_list = line_bot_api.get_rich_menu_list()

#總結
import requests
import json

# ====================================================
'''
這區不能刪掉
'''

token = 'mxJdY40QwXP/pQR6Vilr8J7fBdsLD9E6whHFlUL0Z+XC5BtQtRI1ZKBg/PTpnTYSINtaFnMEcwu7ZKnHjrFnI4mcRnHMr3bwpq9xuBruXPnQRktRkwtTZESrRieAmVW0Rn/NxuQfWNTaKwhxSfgXqgdB04t89/1O/w1cDnyilFU='

headers = {"Authorization":"Bearer mxJdY40QwXP/pQR6Vilr8J7fBdsLD9E6whHFlUL0Z+XC5BtQtRI1ZKBg/PTpnTYSINtaFnMEcwu7ZKnHjrFnI4mcRnHMr3bwpq9xuBruXPnQRktRkwtTZESrRieAmVW0Rn/NxuQfWNTaKwhxSfgXqgdB04t89/1O/w1cDnyilFU=" , "Content-Type":"application/json"}

# ====================================================
'''
Step 1 : 設定一次就可以註解掉了
'''

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "false",
    "name": "Menu",
    "chatBarText": "更多資訊",
    "areas":[
        {
          "bounds": {"x": 113, "y": 45, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "身體資訊"}
        },
        {
          "bounds": {"x": 1321, "y": 45, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "營養素"}
        },
        {
          "bounds": {"x": 113, "y": 910, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "吃"}
        },
        {
          "bounds": {"x": 1321, "y": 910, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "運動gogo"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
# 在這裡要記起 rich_menu_id


# ====================================================
'''
Step 2 : import 要的東西
這段也不能刪掉
'''
from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi(token)
rich_menu_id = 'rich_menu_id'

# ====================================================

"""
設定照片，只能直行過一次
"""
path = r'F:\AI\Line_Chatbot\NutritionBot\menu.jpg'

with open(path, 'rb') as f:
    line_bot_api.set_rich_menu_image(rich_menu_id, "image/png", f)
    
# ====================================================


req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+rich_menu_id,
                       headers=headers)
print(req.text)

rich_menu_list = line_bot_api.get_rich_menu_list()


# ====================================================
"""
上面要重新設定的話要把 ID 刪掉重來
"""

# line_bot_api.delete_rich_menu(rich_menu_id)
