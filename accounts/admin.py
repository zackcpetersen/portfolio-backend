from django.contrib import admin

from accounts.models import SocialLink

admin.site.register(SocialLink, admin.ModelAdmin)
