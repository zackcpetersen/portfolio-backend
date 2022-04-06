from django.core.exceptions import ImproperlyConfigured

from portfolio_backend.settings.base import *


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)


"""
Any settings that are wrapped in eval() should be set as boolean values.

They are returned as strings from the env, and anything other than an 
empty string will result in True, including 'False'
"""

# Django settings
DEBUG = eval(get_env_variable('DEBUG'))
SECRET_KEY = get_env_variable('SECRET_KEY')
# Any env variable with a `.split(" ")` should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = get_env_variable('DJANGO_ALLOWED_HOSTS').split(" ")
CORS_ORIGIN_ALLOW_ALL = eval(get_env_variable('CORS_ORIGIN_ALLOW_ALL'))
CORS_ORIGIN_WHITELIST = get_env_variable('CORS_ORIGIN_WHITELIST').split(" ")
SECURE_SSL_REDIRECT = eval(get_env_variable('SECURE_SSL_REDIRECT'))

# Automatic User Creation
DJANGO_SUPERUSER_EMAIL = get_env_variable('DJANGO_SUPERUSER_EMAIL')
DJANGO_SUPERUSER_PASSWORD = get_env_variable('DJANGO_SUPERUSER_PASSWORD')

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'HOST': get_env_variable('DB_HOST'),
        'PORT': get_env_variable('DB_PORT')
    }
}

# AWS settings
AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_env_variable('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# s3 static settings

USE_S3 = eval(get_env_variable('USE_S3'))
if USE_S3:
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = get_env_variable('STATICFILES_STORAGE')
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = get_env_variable('DEFAULT_FILE_STORAGE')
