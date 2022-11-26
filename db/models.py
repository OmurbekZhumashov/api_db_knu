from statistics import mode
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 20, verbose_name = 'Имя')
    firstName = models.CharField(max_length = 50, verbose_name = 'Фамилия')
    birthday = models.DateField(verbose_name = 'Дата рождения')
    male = models.CharField(max_length = 20, verbose_name = 'Пол')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Люди'
        verbose_name_plural = 'Люди'