from django.contrib import admin

from projects.models import Project, ProjectDescription, ProjectImage, ProjectTag, Tag

admin.site.register(Project, admin.ModelAdmin)
admin.site.register(ProjectDescription, admin.ModelAdmin)
admin.site.register(ProjectImage, admin.ModelAdmin)
admin.site.register(ProjectTag, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
