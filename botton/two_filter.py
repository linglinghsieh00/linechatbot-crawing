'''
為了要標記接下來回覆的選擇地區按鈕樣板訊息(Buttons template message)為第一步驟，
就能夠引用「PostbackEvent」及「PostbackTemplateAction」，在每個選項中增加一個回傳值(data)，
其中夾帶自訂的資料A(代表第一步驟)以及該選項的資料
當使用者選擇地區後，LINE Bot就能夠收到傳值(data)中的資料，讓開發人員可以更有彈性的應用，
其中一個就是可以再新增第二個步驟－「選擇美食分類」，而在其中的每個選項夾帶第一步驟中使用者所選擇的地區資料
'''
'''
一般在傳送文字訊息時，都是MessageEvent(訊息事件)，而如果有回傳值(data)，就會是PostbackEvent(回傳值事件)
所以第一次使用者發送「哈囉」訊息時，沒有回傳值，判斷為MessageEvent，回覆選擇地區的按鈕樣板訊息(Buttons template message)，
第二次當使用者選擇後，由於選項中有回傳值(data)，因此判斷PostbackEvent就會成立。
接著，利用Python的字串切割，判斷為A(第一步驟)，所以將回傳值(data)中使用者選擇的地區附加到B(第二步驟)的回傳值(data)中，
並且回覆選擇餐廳分類的鈕樣板訊息(Buttons template message)。
使用者在選擇餐廳分類後，同樣為PostbackEvent，所以LINE Bot就可以從回傳值(data)中取得使用者在第一及第二步驟所選擇的資料了。
'''

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent, 
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    PostbackEvent,
    PostbackTemplateAction)

from .scraper import IFoodie

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
            print(events)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
                                                                                                                 
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if event.message.text == "Hi":
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='請選擇地區',
                                actions=[
                                    PostbackTemplateAction(
                                        label='台北市',
                                        text='台北市',
                                        data='A&台北市'
                                    ),
                                    PostbackTemplateAction(
                                        label='台中市',
                                        text='台中市',
                                        data='A&台中市'
                                    ),
                                    PostbackTemplateAction(
                                        label='高雄市',
                                        text='高雄市',
                                        data='A&高雄市'

                                    )
                                ]
                            )
                        )
                    )
            elif isinstance(event, PostbackEvent):  # 如果有回傳值事件
                if event.postback.data[0:1] == "A":  # 如果回傳值為「選擇地區」         
                    area = event.postback.data[2:]  # 透過切割字串取得地區文字
                    line_bot_api.reply_message(  # 回應前五間最高人氣且營業中的餐廳訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='請選擇美食類別',
                                actions=[
                                    PostbackTemplateAction(  # 將第一步驟選擇的地區，包含在第二步驟的資料中
                                        label='火鍋',
                                        text='火鍋',
                                        data='B&' + area + '&火鍋'
                                    ),
                                    PostbackTemplateAction(
                                        label='早午餐',
                                        text='早午餐',
                                        data='B&' + area + '&早午餐'
                                    ),
                                    PostbackTemplateAction(
                                        label='約會餐廳',
                                        text='約會餐廳',
                                        data='B&' + area + '&約會餐廳'
                                    )
                                ]
                            )
                        )
                    )
                elif event.postback.data[0:1] == "B":  # 如果回傳值為「選擇美食類別」
 
                        result = event.postback.data[2:].split('&')  # 回傳值的字串切割
                        food = IFoodie(
                        result[0],  # 地區
                        result[1]  # 美食類別
                        )
                        line_bot_api.reply_message(  # 回復訊息文字
                            event.reply_token,
                        # 爬取該地區正在營業，且符合所選擇的美食類別的前五大最高人氣餐廳
                        TextSendMessage(text=food.scrape())
                        )

                            
                        
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
      
      
    #增加了一個美食分類，所以在scraper.py網頁爬蟲檔案中，Food抽象類別的建構式，需增加category屬性
    # 美食抽象類別
class Food(ABC):
 
    def __init__(self, area, category):
        self.area = area  # 地區
        self.category = category  # 美食類別
 
    @abstractmethod
    def scrape(self):
        pass
      
    # 愛食記爬蟲
class IFoodie(Food):
 
    def scrape(self):
        response = requests.get(
            "https://ifoodie.tw/explore/" + self.area +
            "/list/" + self.category +
            "?sortby=popular&opening=true")
 
        soup = BeautifulSoup(response.content, "html.parser")
 
        # 爬取前五筆餐廳卡片資料
        cards = soup.find_all(
            'div', {'class': 'jsx-1776651079 restaurant-info'}, limit=5)
 
        content = ""
        for card in cards:
 
            title = card.find(  # 餐廳名稱
                "a", {"class": "jsx-1776651079 title-text"}).getText()
 
            stars = card.find(  # 餐廳評價
                "div", {"class": "jsx-1207467136 text"}).getText()
 
            address = card.find(  # 餐廳地址
                "div", {"class": "jsx-1776651079 address-row"}).getText()
 
            content += f"{title} \n{stars}顆星 \n{address} \n\n"
 
        return content
