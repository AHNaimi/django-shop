from django.contrib import admin
from .models import OrderModel, Paymodel

admin.site.register(OrderModel)
admin.site.register(Paymodel)