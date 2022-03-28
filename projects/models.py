from django.db import models
from django.utils.text import slugify

from accounts.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)
    source = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)
    description = models.CharField(max_length=999999)
    slug = models.SlugField(editable=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class ProjectImage(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT,
                                related_name='images')
    image = models.ImageField(upload_to='project-images')
    featured = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    description = models.CharField(max_length=2000)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project', 'tag'], name='Project Tag Unique')
        ]

    def __str__(self):
        return f'{self.tag.name} - {self.project}'
