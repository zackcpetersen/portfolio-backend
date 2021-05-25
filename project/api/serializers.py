from rest_framework import serializers

from project.models import Project, ProjectDescription, ProjectImage, ProjectTag


class ProjectDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDescription
        fields = '__all__'


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'


class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True)
    descriptions = ProjectDescriptionSerializer(many=True)
    tags = ProjectTagSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'user', 'source', 'live_url',
                  'images', 'descriptions', 'tags']
