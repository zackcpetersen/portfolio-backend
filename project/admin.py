from django.contrib import admin

from project.models import Project, ProjectDescription, ProjectImage, ProjectTag

admin.site.register(Project, admin.ModelAdmin)
admin.site.register(ProjectDescription, admin.ModelAdmin)
admin.site.register(ProjectImage, admin.ModelAdmin)
admin.site.register(ProjectTag, admin.ModelAdmin)
