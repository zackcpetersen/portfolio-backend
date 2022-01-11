from django.contrib import admin

from accounts.models import ContactRequest, SocialLink, User

admin.site.register(ContactRequest, admin.ModelAdmin)
admin.site.register(SocialLink, admin.ModelAdmin)
admin.site.register(User, admin.ModelAdmin)
