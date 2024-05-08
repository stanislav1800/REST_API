from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone_nombers', 'fam', 'name', 'otc']


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()
    class Meta:
        model = Images
        fields = ['data', 'title']


class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coord = CoordSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)


    class Meta:
        model = Pereval
        depth = 1
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level', 'images', 'status']
        read_only_fields = ['status']