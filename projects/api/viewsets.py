from rest_framework import viewsets

from projects.api.serializers import ProjectSerializer
from projects.models import Project


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
