from django.db import models
from django.utils.text import slugify

from accounts.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255, unique=True)
    live_url = models.URLField()
    order = models.PositiveSmallIntegerField(default=99)
    description = models.CharField(max_length=999999)
    slug = models.SlugField(editable=False, unique=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article-images')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.article}'
