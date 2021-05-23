from django.contrib import admin

from accounts.models import SocialLink, User

admin.site.register(SocialLink, admin.ModelAdmin)
admin.site.register(User, admin.ModelAdmin)
