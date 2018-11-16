from django.contrib import admin
from .import models

from .models import Question, Category, Product

admin.site.register(Question)

@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_editable = ('price',)
    list_display = ('category', 'name', 'price', 'get_prev')
    list_filter = ('category', 'price')
    list_display_links = ('get_prev', 'name')
