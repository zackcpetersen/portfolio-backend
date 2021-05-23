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
        fields = ['user', 'source', 'live_url', 'images', 'descriptions', 'tags']

    # def get_images(self, project):
    #     return project.images.values_list('image', flat=True)
    #
    # def get_descriptions(self, project):
    #     return project.descriptions.values_list()
    #
    # def get_tags(self, project):
    #     return project.tags.all()
