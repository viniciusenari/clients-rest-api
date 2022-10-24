from django.contrib import admin
from clients.models import Client

class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','ssn', 'phone', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 25

admin.site.register(Client, Clients)

