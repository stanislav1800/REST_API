from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
import django_filters
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


class UserViewset(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UsersSerializer

class CoordsViewSet(viewsets.ModelViewSet):
   queryset = Coords.objects.all()
   serializer_class = CoordSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    ilter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['beauty_title', 'title', 'add_time', 'user__email']

    def create(self, request, *args, **kwargs):
        if self.action == 'create':
           serializer = PerevalSerializer(data=request.data)

           if serializer.is_valid():
               serializer.save()
               return Response(
                   {
                       'status': status.HTTP_200_OK,
                       'message': 'Успех!',
                       'id': serializer.instance.pk,
                   }
               )

           if status.HTTP_400_BAD_REQUEST:
               return Response(
                   {
                       'status': status.HTTP_400_BAD_REQUEST,
                       'message': 'Некорректный запрос',
                       'id': None,
                   }
               )

           if status.HTTP_500_INTERNAL_SERVER_ERROR:
               return Response(
                   {
                       'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Ошибка при выполнении операции',
                       'id': None,
                   }
               )
        return super().create(request, *args, **kwargs)

    # def update(self, instance, validated_data):
    #    user = validated_data.pop('user')
    #    coord = validated_data.pop('coords')
    #    level = validated_data.pop('level')
    #    images = validated_data.pop('images')
    #
    #    user = User.objects.update(**user)
    #    coord = Coords.objects.update(**coord)
    #    level = Level.objects.update(**level)
    #
    #    for image in images:
    #        data = image.pop('data')
    #        title = image.pop('title')
    #        PerevalImages.objects.update(data=data, title=title)
    #
    #    return super().update(instance, validated_data)

