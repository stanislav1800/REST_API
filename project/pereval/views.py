from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *
from .models import *


class UserViewset(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UsersSerializer
   permission_classes = [permissions.IsAuthenticated]

class CoordsViewSet(viewsets.ModelViewSet):
   queryset = Coords.objects.all()
   serializer_class = CoordSerializer
   permission_classes = [permissions.IsAuthenticated]


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [permissions.IsAuthenticated]


class PerevalViewset(viewsets.ModelViewSet):
   queryset = Pereval.objects.all()
   serializer_class = PerevalSerializer


