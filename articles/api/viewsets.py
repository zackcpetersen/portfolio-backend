from rest_framework import viewsets

from articles.api.serializers import ArticleSerializer, ArticleImageSerializer
from articles.models import Article, ArticleImage


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('order')
    serializer_class = ArticleSerializer
    lookup_field = 'slug'


class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer
