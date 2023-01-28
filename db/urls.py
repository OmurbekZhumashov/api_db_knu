import imp
from xml.etree.ElementInclude import include
from django.urls import path, include

from .views import *
from rest_framework import routers
app_name = 'person'


urlpatterns = [
    path('glossary/view/all/', GlossaryListView.as_view()),#Получение всех объектов
    path('glossary/create/', GlossaryListView.as_view()),#Добавление нового объекта
    path('glossary/detail/<int:pk>/', GlossaryAPIDetail.as_view()),#Изменение и удаление


]
