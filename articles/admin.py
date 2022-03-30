from django.contrib import admin

from articles.models import Article, ArticleImage

admin.site.register(Article, admin.ModelAdmin)
admin.site.register(ArticleImage, admin.ModelAdmin)
