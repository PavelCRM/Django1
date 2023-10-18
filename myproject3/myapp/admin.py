from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'added_date', 'display_photo')

    def display_photo(self, obj):
        return '<img src="{0}" style="max-height: 100px; max-width: 100px;" />'.format(obj.photo.url)

    display_photo.allow_tags = True
    display_photo.short_description = 'Фото'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_amount', 'order_date')

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
