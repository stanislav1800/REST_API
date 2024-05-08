from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *
from .models import *


class UserViewset(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UsersSerializer

class CoordsViewSet(viewsets.ModelViewSet):
   queryset = Coords.objects.all()
   serializer_class = CoordSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = LevelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewset(viewsets.ModelViewSet):
   queryset = Pereval.objects.all()
   serializer_class = PerevalSerializer


