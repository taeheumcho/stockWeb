from django.contrib import admin
from models import ZzImsiSisae
from stockInfo.models import ImsiIndexData, CcImsiData
# Register your models here.
admin.register(ZzImsiSisae)
admin.register(ImsiIndexData)
admin.register(CcImsiData)