from django.contrib import admin

# Register your models here.

from .models import DNSRECORD

@admin.register(DNSRECORD)
class DNSRECORDAdmin(admin.ModelAdmin):
    list_display = ['id', 'zone', 'domain', 'type', 'target', 'target_slave_flag', 'charge_person']
    list_filter = ['zone', 'domain', 'charge_person']
    list_editable = ['domain', 'target', 'charge_person']

