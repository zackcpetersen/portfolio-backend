from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from accounts.api.serializers import ContactRequestSerializer, UserSerializer
from accounts.models import ContactRequest, User


class ContactRequestViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
