from rest_framework import routers

from presentations.api import viewsets as presentation_views

router = routers.DefaultRouter()

router.register(r'presentations', presentation_views.PresentationViewSet)
