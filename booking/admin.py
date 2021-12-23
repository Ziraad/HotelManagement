from django.contrib import admin

from .models import Booking, Rooms

admin.site.register(Rooms)
admin.site.register(Booking)
