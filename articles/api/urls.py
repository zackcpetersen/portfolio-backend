from rest_framework import routers

from articles.api import viewsets as article_views

router = routers.DefaultRouter()

router.register(r'articles', article_views.ArticleViewSet)
router.register(r'article-images', article_views.ArticleImageViewSet)
