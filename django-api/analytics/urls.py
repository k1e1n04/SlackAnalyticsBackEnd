from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    # 組織(ワークスペース)の一覧
    path('organization/list/',views.OrganizaionList.as_view()),
    # 拠点の一覧
    path('base/list/',views.BaseList.as_view()),

]