from rest_framework import serializers

from presentations.models import Presentation


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'
