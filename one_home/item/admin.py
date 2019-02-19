"""Adds models to the admin page."""
from django.contrib import admin
from .models import Item, Room, Buyer, Cart

# Register your models here.

admin.site.register(Item)
admin.site.register(Room)
admin.site.register(Buyer)
admin.site.register(Cart)
