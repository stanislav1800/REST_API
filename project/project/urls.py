"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pereval import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewset)
router.register(r'coords', views.CoordsViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'image', views.ImageViewSet)
router.register(r'pereval', views.PerevalViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pereval.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
