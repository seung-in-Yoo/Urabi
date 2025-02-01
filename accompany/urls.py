from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accompany'

urlpatterns = [
    path('', views.AccompanyListView.as_view(), name='accompany_list'),
    path('detail', views.accompany_detail, name='accompany_detail'),
    path('create', views.accompany_create, name='accompany_create'),
]
