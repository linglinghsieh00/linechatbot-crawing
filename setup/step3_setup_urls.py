#foodlinebot/urls.py，加入以下網址設定
from django.urls import path
from . import views
 
urlpatterns = [
    path('callback', views.callback)
]


#將這個 APP 網址加到專案主程式中，所以在 mylinebot/urls.py 檔案中加入下面網址設定
from django.contrib import admin
from django.urls import path, include # 引用include函式

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodlinebot/', include('foodlinebot.urls')) #包含應用程式的網址
]
'''
透過include函式，即可將應用程式(APP)中的所有網址註冊到Django專案主程式(potrip)中，當使用者存取http://127.0.0.1:8000/posts/開頭的網址時，
Django就知道要去找posts應用程式(APP)中的網址。'''
