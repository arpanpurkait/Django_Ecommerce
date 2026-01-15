from django.contrib import admin
from .models import Cart, CartItem   # adjust model names if needed

admin.site.register(Cart)
admin.site.register(CartItem)
