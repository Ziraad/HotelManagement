from django.contrib import admin

from .models import Booking, Rooms


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ['room_no', 'is_available', 'no_of_days_advance']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['room_no', 'start_day', 'end_day']
