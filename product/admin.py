from django.contrib import admin

# Register your models here.

from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    list_filter = ['category',]
    search_fields = ['product']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)