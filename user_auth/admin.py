# user_auth/admin.py

from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('id', 'full_name', 'nip', 'role', 'email')
    list_filter = ('role',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'nip', 'role')}),
    )
    search_fields = ('email', 'full_name')
    ordering = ('-id',)

admin.site.register(CustomUser, CustomUserAdmin)
