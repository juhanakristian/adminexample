from django.contrib import admin
from .models import Item

from decimal import Decimal


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "vat", "is_available")
    list_editable = ("is_available",)

    def vat(self, obj: Item) -> str:
        return f"{(obj.price * Decimal(0.05)):.2f}$"


admin.site.register(Item, ItemAdmin)
