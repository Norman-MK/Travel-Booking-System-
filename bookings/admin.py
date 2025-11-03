from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','trip','seats_booked','booked_at')
    list_filter = ('booked_at',)
