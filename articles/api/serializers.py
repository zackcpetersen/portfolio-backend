from rest_framework import serializers

from articles.models import Article, ArticleImage


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    images = ArticleImageSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'
