from django.contrib import admin
from UserApp.models import *
# Register your models here.

@admin.register(BioUser)
class ListBio(admin.ModelAdmin):
    list_display = ['custom_id', 'birth_place', 'birth_date', 'address', 'religion']
    search_fields = ['birth_place', 'birth_date', 'religion', 'address']
    list_filter = ['birth_place', 'religion']
    readonly_fields = ['custom_id']
    list_per_page = 10


@admin.register(SecretKey)
class ListSecretKey(admin.ModelAdmin):
    list_display = ['secret_key', 'add_secret', 'expiry_secret', 'user']
    search_fields = ['secret_key', 'add_secret', 'expiry_secret']
    list_filter = ['secret_key']
    list_per_page = 10