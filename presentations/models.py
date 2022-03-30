from django.db import models
from django.utils.text import slugify

from accounts.models import User


class Presentation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)
    order = models.PositiveSmallIntegerField(default=99)
    image = models.ImageField(upload_to='presentation-images')
    slug = models.SlugField(editable=False, unique=True)
    description = models.CharField(max_length=2048)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Presentation, self).save(*args, **kwargs)
