from django.contrib import admin

# Register your models here.

from .models import Event, EventRequest

admin.site.register(Event)
admin.site.register(EventRequest)
