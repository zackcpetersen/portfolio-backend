from rest_framework import routers

from accounts.api import viewsets as account_views

router = routers.DefaultRouter()

router.register(r'contact', account_views.ContactRequestViewSet)
router.register(r'users', account_views.UserViewSet)
