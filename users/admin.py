from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Personnel

# Customize the UserAdmin to handle the custom fields of Personnel
class PersonnelAdmin(UserAdmin):
    model = Personnel
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('teams',)}),  # Add the teams field to the form
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('teams',)}),  # Add the teams field for user creation
    )
    filter_horizontal = ('teams',)  # Allows better multi-selection UI for teams

# Register Personnel in the admin
admin.site.register(Personnel, PersonnelAdmin)

