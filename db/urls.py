import imp
from xml.etree.ElementInclude import include
from django.urls import path, include

from .views import *
from rest_framework import routers
app_name = 'person'


urlpatterns = [
    path('person/view/all/', PersonListView.as_view()),#Получение всех объектов
    path('person/create/', PersonListView.as_view()),#Добавление нового объекта
    path('person/detail/<int:pk>/', PersonAPIDetail.as_view()),#Изменение и удаление


]
