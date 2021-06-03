from rest_framework import mixins, viewsets

from accounts.api.serializers import ContactRequestSerializer, UserSerializer
from accounts.models import ContactRequest, User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactRequestViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer
