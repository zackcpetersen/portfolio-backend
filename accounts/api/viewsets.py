from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers import SocialLinkSerializer
from accounts.models import SocialLink


class SocialLinkViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
