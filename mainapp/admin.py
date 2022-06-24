from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Bolim, Mahsulot, Ichki
admin.site.register(Bolim)
admin.site.register(Ichki)
@admin.register(Mahsulot)
class MahsulotAdmin(ModelAdmin):
    search_fields = ['__all__']


