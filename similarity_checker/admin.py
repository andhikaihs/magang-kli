from django.contrib import admin
from .models import InstagramCaption

@admin.register(InstagramCaption)
class InstagramCaptionAdmin(admin.ModelAdmin):
    list_display = ('account', 'agenda', 'caption', 'posted_date_time')
    search_fields = ('account__account_url', 'agenda__topik_agenda')
    readonly_fields = ('caption', 'posted_date_time')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
