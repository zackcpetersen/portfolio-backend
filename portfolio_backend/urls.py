"""portfolio_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from accounts.api.urls import router as accounts_router
from presentations.api.urls import router as presentations_router
from projects.api.urls import router as projects_router

router = routers.DefaultRouter()
router.registry.extend(accounts_router.registry)
router.registry.extend(presentations_router.registry)
router.registry.extend(projects_router.registry)

api_url_patterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
