'''
Template Message 種類
Buttons，一般的按鈕
Confirm，確認按鈕
Carousel，可以橫向滑動的多選項按鈕
Image Carousel，多影像按鈕。
'''
'''
我們做一個 Button，有兩個選項：
是，第一次見面：點選後會回傳是。
已經見過了：點選後會回傳見過了。
'''
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            print("event", event.message.id)
            # print("event", type(event))
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                print("message", event.message)
                message = []

                if event.message.type == 'text':
                    mtext = event.message.text
                    if "嗨" in mtext:
                        message.append(
                            TemplateSendMessage(
                                alt_text='Buttons template',
                                template=ButtonsTemplate(
                                    title='Hello',
                                    text='第一次見面嗎',
                                    actions=[
                                        MessageTemplateAction(
                                            label='是，第一次見面',
                                            text='是',
                                        ),
                                        MessageTemplateAction(
                                            label='已經見過了',
                                            text='見過了',
                                        ),
                                    ]
                                )
                            )
                        )



                    print("type of mtext: {}".format(type(mtext)))

                # 回復傳入的訊息文字
                line_bot_api.reply_message( event.reply_token, message )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
        
 # Buttons template 的 json example，官方提供的範例顯示了所有可以使用的屬性（attribute）
 {
  "type": "template",
  "altText": "This is a buttons template",
  "template": {
      "type": "buttons",
      "thumbnailImageUrl": "https://example.com/bot/images/image.jpg",
      "imageAspectRatio": "rectangle",
      "imageSize": "cover",
      "imageBackgroundColor": "#FFFFFF",
      "title": "Menu",
      "text": "Please select",
      "defaultAction": {
          "type": "uri",
          "label": "View detail",
          "uri": "http://example.com/page/123"
      },
      "actions": [
          {
            "type": "postback",
            "label": "Buy",
            "data": "action=buy&itemid=123"
          },
          {
            "type": "postback",
            "label": "Add to cart",
            "data": "action=add&itemid=123"
          },
          {
            "type": "uri",
            "label": "View detail",
            "uri": "http://example.com/page/123"
          }
      ]
  }
}

#template：這裡對應到 json 裡的
#titile：標題
#text：副標題
#label：bottom 鍵內容
'''
actions：就是包含主體 按鈕，還有按下去的要做的動作。有多種選項可以選擇。
Postback action
Message action
URI action
Datetime picker action
Camera action
Camera roll action
Location action
Richmenu Switch Action
'''
#不過我主要都使用 Message action 而以，所以我們目前也只針對這個。
MessageTemplateAction(
    label='是，第一次見面',
    text='是',
),
#text，表示當你點選按鈕後送出之後會傳送出去的字。
#但是要注意！按鈕最多只能放四個，就是 actions 裡面只能有四個。

