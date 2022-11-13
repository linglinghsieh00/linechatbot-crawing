將原本的文字回應訊息，調整為按鈕樣板訊息(Buttons template message)，在對談互動的過程中，讓使用者透過按鈕選擇的方式，
提供所在的地區及想要吃的美食分類，接著，在LINE Bot中利用Python網頁爬蟲取得符合需求的前五個最高人氣且營業中的餐廳。

![IMG_CC991868A5D5-1](https://user-images.githubusercontent.com/102644365/201522838-94615b5a-3118-4bb6-a9f9-eb0032bb6062.jpeg)

LINE Bot判斷使用者發送「Hi」訊息時，在replay_message(回覆訊息)的API中，使用TemplateSendMessage(樣板傳送訊息)，並且指定為Buttons Template(按鈕樣板)。其中就可以自訂標題、文字及按鈕。
當使用者選擇地區後，判斷使用者發送的訊息不是「哈囉」，將地區傳入Python網頁爬蟲中取得資料。


