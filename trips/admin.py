from django.contrib import admin
from .models import Trip

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title','destination','price','available_seats','start_date')
    search_fields = ('title','destination')
