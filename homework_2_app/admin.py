from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_registration']

    fields = ['name', 'email', 'phone', 'address', 'date_registration']
    readonly_fields = ['date_registration']


class ProductAdmin(admin.ModelAdmin):
    def short_description(self, obj):
        return obj.description[:35] + '...' if len(obj.description) > 35 else obj.description

    short_description.short_description = 'Product'
    list_display = ['name', 'short_description', 'count', 'date_added']
    ordering = ['-count']
    list_filter = ['date_added', 'price']
    search_fields = ['name']
    search_help_text = 'Поиск по имени продукта'

    fields = ['name', 'description', 'price', 'count', 'date_added', 'image']
    readonly_fields = ['date_added']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']
    ordering = ['date_ordered']
    list_filter = ['date_ordered']

    fields = ['customer', 'products', 'total_price', 'date_ordered']
    readonly_fields = ['customer', 'products', 'total_price', 'date_ordered']


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
