from django.contrib import admin
from .models import Location,Event,Event_member

# Register your models here.

admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Event_member)
