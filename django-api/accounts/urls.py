from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [    
    # 現在ログインしているユーザー
    path('user',views.CurrentUser.as_view()),
]