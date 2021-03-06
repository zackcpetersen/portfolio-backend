from rest_framework import routers

from projects.api import viewsets as project_views

router = routers.DefaultRouter()

router.register(r'projects', project_views.ProjectViewSet)
router.register(r'tags', project_views.TagViewSet)
