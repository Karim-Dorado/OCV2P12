from django.contrib import admin
from api.models import Client, Contract, Event

# Register your models here.
admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
