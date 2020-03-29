from django.contrib import admin
from .models import HostUser, HostBoard
# Register your models here.
admin.site.register(HostUser)
admin.site.register(HostBoard)