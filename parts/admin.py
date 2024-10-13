from django.contrib import admin
from .models import Part

class PartAdmin(admin.ModelAdmin):
    list_display = ('part_type', 'aircraft_type', 'team', 'created_at')
    list_filter = ('part_type', 'aircraft_type', 'team')
    search_fields = ('part_type', 'aircraft_type__aircraft_type', 'team__team_type')

admin.site.register(Part, PartAdmin)

