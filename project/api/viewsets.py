from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from project.api.serializers import ProjectSerializer, ProjectDescriptionSerializer, \
    ProjectImageSerializer, ProjectTagSerializer
from project.models import Project, ProjectDescription, ProjectImage, ProjectTag


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# TODO can remove all below - all the info that's needed comes from project serializer
class ProjectDescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProjectDescription.objects.all()
    serializer_class = ProjectDescriptionSerializer


class ProjectImageViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer


class ProjectTagViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProjectTag.objects.all()
    serializer_class = ProjectTagSerializer
