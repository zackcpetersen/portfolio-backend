from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.is_staff = True
        user.is_superuser = True
        user.pass_valid = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **kwargs):
        return self.create_user(**kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='Email Address',
                              max_length=255, unique=True,
                              db_index=True)
    phone = models.CharField(max_length=12, unique=True)
    bio = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='profile-images',
                              null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return f'{self.name} - {self.email}'


class SocialLink(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='social_links')
    name = models.CharField(max_length=255)
    link = models.URLField()
    icon = models.CharField(max_length=255, help_text='Use material design icons prepended with "mdi-", '
                                                      'see full list at https://materialdesignicons.com/')

    def __str__(self):
        return self.name
