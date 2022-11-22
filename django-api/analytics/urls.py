from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('organization/list/',views.OrganizaionList.as_view()),

]