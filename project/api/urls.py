from rest_framework import routers

from project.api import viewsets as project_views

router = routers.DefaultRouter()

router.register(r'projects', project_views.ProjectViewSet)
router.register(r'project-descriptions', project_views.ProjectDescriptionViewSet)
router.register(r'project-images', project_views.ProjectImageViewSet)
router.register(r'project-tags', project_views.ProjectTagViewSet)
