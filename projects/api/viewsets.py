from rest_framework import viewsets

from projects.api.serializers import ProjectSerializer, TagSerializer
from projects.models import Project, Tag


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('order')
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
