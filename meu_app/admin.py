from django.contrib import admin
from meu_app.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "quantity", "active", "created_at"]
    list_filter = ["active"]
    search_fields = ["name"]
