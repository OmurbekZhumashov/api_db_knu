
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Glossary(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Называние')
    discraption = models.TextField(verbose_name = 'Описание')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Глоссарий'
        verbose_name_plural = 'Глоссарий'
        