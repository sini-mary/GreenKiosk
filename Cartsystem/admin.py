from django.contrib import admin

# Register your models here.
from .models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ('products','total','image')
admin.site.register(Cart, CartAdmin)
