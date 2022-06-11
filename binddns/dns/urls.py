from django.urls import path
from . import  views

app_name = 'dns'

urlpatterns = [
    path('', views.dns_list, name='dns_list'),
    path('<str:ZONE>/', views.dns_list, name='dns_list_by_zone'),
    path('<str:domain>/<int:id>/', views.dns_detail, name="dns_detail")
]