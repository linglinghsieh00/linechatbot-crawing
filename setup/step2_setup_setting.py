#憑證
LINE_CHANNEL_ACCESS_TOKEN = 'Messaging API > Channel access token'
LINE_CHANNEL_SECRET = 'Basic settings > Channel secret'

#settings.py 檔裡面的 INSTALLED_APPS 加上剛建立的 Django 應用程式
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django_chatbot.apps.DjangoChatbotConfig',    #新增APP名稱
]
