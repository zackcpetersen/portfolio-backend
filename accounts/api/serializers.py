from rest_framework import serializers

from accounts.models import ContactRequest, SocialLink, User


class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        exclude = ['id']


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(read_only=True, many=True)

    class Meta:
        model = User
        exclude = ['password', 'is_active', 'is_staff', 'last_login',
                   'is_superuser', 'groups', 'user_permissions']
