from rest_framework import serializers

from projects.models import Project, ProjectImage, ProjectTag, Tag


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'


class ProjectTagSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ProjectTag
        fields = '__all__'

    def get_name(self, project_tag):
        return project_tag.tag.name


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True)
    tags = ProjectTagSerializer(many=True)
    all_tags = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'user', 'source', 'live_url',
                  'images', 'description', 'tags', 'all_tags']

    def get_all_tags(self, project):
        return project.tags.values_list('tag__name', flat=True)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
