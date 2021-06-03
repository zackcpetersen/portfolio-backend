from django.db import models

from accounts.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)
    source = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    # slug for url? autogenerate - UNIQUE

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT,
                                related_name='images')
    image = models.ImageField(upload_to='project-images')
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)


class ProjectDescription(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='descriptions')
    title = models.CharField(max_length=50, unique=True)
    info = models.CharField(max_length=10000)
    order = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return '{} - {}'.format(self.project, self.info[:75])


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    description = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.tag.name, self.project)
