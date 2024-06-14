from django.contrib import admin
from baskets.models import Basket

# Register your models here.


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'create_timestamp', 'update_timestamp')
    readonly_fields = ('create_timestamp', 'update_timestamp')
    extra = 0
