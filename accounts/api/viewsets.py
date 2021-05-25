from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers import SocialLinkSerializer, UserSerializer
from accounts.models import SocialLink, User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SocialLinkViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
