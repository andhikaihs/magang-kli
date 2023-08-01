from django.contrib import admin
from .models import SocmedData, Instagram, Linkedin, Youtube, Tiktok, Facebook, Twitter

class SocmedDataAdmin(admin.ModelAdmin):
    list_display = ['ue1', 'account_url', ]
    list_filter = ['ue1']
    search_fields = ['account_url',]

class InstagramAdmin(SocmedDataAdmin):
    # Add any additional customizations specific to Instagram here
    pass

class LinkedinAdmin(SocmedDataAdmin):
    # Add any additional customizations specific to Linkedin here
    pass

class YoutubeAdmin(SocmedDataAdmin):
    # Add any additional customizations specific to Youtube here
    pass

class TiktokAdmin(SocmedDataAdmin):
    # Add any additional customizations specific to Tiktok here
    pass

class FacebookAdmin(SocmedDataAdmin):
    # Add any additional customizations specific to Facebook here
    pass

class TwitterAdmin(SocmedDataAdmin):
    # Add any additional customizations specific to Twitter here
    pass

# Register the models with their respective admin classes
admin.site.register(SocmedData, SocmedDataAdmin)
admin.site.register(Instagram, InstagramAdmin)
admin.site.register(Linkedin, LinkedinAdmin)
admin.site.register(Youtube, YoutubeAdmin)
admin.site.register(Tiktok, TiktokAdmin)
admin.site.register(Facebook, FacebookAdmin)
admin.site.register(Twitter, TwitterAdmin)
