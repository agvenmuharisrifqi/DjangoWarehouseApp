from django.contrib import admin
from ProductApp.models import *


# Register your models here.
@admin.register(Suplier)
class ListSuplier(admin.ModelAdmin):
    list_display = ['custom_id', 'name', 'suplier', 'email', 'address']
    search_fields = ['name', 'suplier', 'address']
    list_filter = ['name', 'suplier']
    readonly_fields = ['custom_id']
    list_per_page = 10

@admin.register(Product)
class ListProduct(admin.ModelAdmin):
    list_display = ['custom_id', 'name', 'number', 'purchase', 'selling', 'stock', 'company']
    search_fields = ['name', 'number', 'company', 'stock']
    list_filter = ['name', 'number', 'company', 'stock']
    readonly_fields = ['custom_id']
    list_per_page = 10

@admin.register(PurchaseOrder)
class ListPurchaseOrder(admin.ModelAdmin):
    list_display = ['custom_id', 'number', 'date', 'company', 'name', 'address', 'note']
    search_fields = ['number', 'company', 'name']
    list_filter = ['number', 'company', 'name']
    readonly_fields = ['custom_id']
    list_per_page = 10

@admin.register(Order)
class ListOrder(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'number']
    search_fields = ['product', 'quantity', 'number']
    list_filter = ['product', 'quantity', 'number']
    list_per_page = 10