#把 template= 改成 ConfirmTemplate
if event.message.type == 'text':
    mtext = event.message.text
    if "嗨" in mtext:
        message.append(
            TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='有看懂嗎',
                        actions=[
                        MessageTemplateAction(
                            label='Yes',
                            text='Yes',
                        ),
                        MessageTemplateAction(
                            label='No',
                            text='No',
                        )
                    ]
                )
            )
        )

#原本的 json 裡面所有的屬性
{
  "type": "template",
  "altText": "this is a confirm template",
  "template": {
      "type": "confirm",
      "text": "Are you sure?",
      "actions": [
          {
            "type": "message",
            "label": "Yes",
            "text": "yes"
          },
          {
            "type": "message",
            "label": "No",
            "text": "no"
          }
      ]
  }
}


#以橫向選擇的多排按鈕
{
  "type": "template",
  "altText": "this is a carousel template",
  "template": {
      "type": "carousel",
      "columns": [
          {
            "thumbnailImageUrl": "https://example.com/bot/images/item1.jpg",
            "imageBackgroundColor": "#FFFFFF",
            "title": "this is menu",
            "text": "description",
            "defaultAction": {
                "type": "uri",
                "label": "View detail",
                "uri": "http://example.com/page/123"
            },
            "actions": [
                {
                    "type": "postback",
                    "label": "Buy",
                    "data": "action=buy&itemid=111"
                },
                {
                    "type": "postback",
                    "label": "Add to cart",
                    "data": "action=add&itemid=111"
                },
                {
                    "type": "uri",
                    "label": "View detail",
                    "uri": "http://example.com/page/111"
                }
            ]
          },
          {
            "thumbnailImageUrl": "https://example.com/bot/images/item2.jpg",
            "imageBackgroundColor": "#000000",
            "title": "this is menu",
            "text": "description",
            "defaultAction": {
                "type": "uri",
                "label": "View detail",
                "uri": "http://example.com/page/222"
            },
            "actions": [
                {
                    "type": "postback",
                    "label": "Buy",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "postback",
                    "label": "Add to cart",
                    "data": "action=add&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "View detail",
                    "uri": "http://example.com/page/222"
                }
            ]
          }
      ],
      "imageAspectRatio": "rectangle",
      "imageSize": "cover"
  }
}
#其餘方式等等都語一般的按鈕模板一樣。
但這裡要注意的是：橫向按鈕模板最多10個；按鈕選像這裡最多只能有3個。
