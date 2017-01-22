from django.contrib import admin
from .models import access_ticket

class access_ticket_admin(admin.ModelAdmin):
    exclude = ('hash_key','acs_date',)
    list_display = ('college','__str__', 'hash_key','acs_date','active')

admin.site.register(access_ticket,access_ticket_admin)
