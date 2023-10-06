from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'title',
        'pub_date',
        'author',
    )
    search_fields = ('text', 'title')
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'