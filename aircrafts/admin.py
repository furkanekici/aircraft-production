from django.contrib import admin
from .models import Aircraft

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('aircraft_type', 'assembled', 'created_at')

