from django.contrib import admin

# Register your models here.

from .models import Admin, UserRequest

admin.site.register(Admin)
admin.site.register(UserRequest)