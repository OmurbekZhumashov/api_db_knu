from django.contrib import admin
from db.models import *
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in Person._meta.fields]


admin.site.register (Person, PersonAdmin)