from rest_framework import viewsets

from presentations.api.serializers import PresentationSerializer
from presentations.models import Presentation


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer
