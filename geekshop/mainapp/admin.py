from django.contrib import admin
from mainapp.models import ProductCategory, Product

# Register your models here
admin.site.register(ProductCategory)
# admin.site.register(Product)


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('price',)
    search_fields = ('name',)
