from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone_nombers']


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
    print('Зашол')
    user = UsersSerializer()
    coords = CoordSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)
    # status = serializers.CharField()

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level', 'images', 'status']


    def create(self, validated_data, **kwargs):
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')
        # beauty_title = validated_data.pop('beauty_title')
        # title = validated_data.pop('title')
        # other_titles = validated_data.pop('other_titles')
        # connect = validated_data.pop('connect')

        user, created = User.objects.get_or_create(**user_data)
        coord_id = Coords.objects.create(**coord_data)
        level_id = Level.objects.create(**level_data)
        images = Level.objects.create(**level_data)

        pereval = Pereval.objects.create(user_id=user.pk, coords_id=coord_id.pk, level_id=level_id.pk, **validated_data)

        for image_data in images_data:
            Images.objects.create(pereval=pereval, **image_data)

        return pereval

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.email != data_user['email'],
                instance_user.fam != data_user['fam'],
                instance_user.name != data_user['name'],
                instance_user.otc != data_user['otc'],
                instance_user.phone_nombers != data_user['phone_nombers']
            ]
            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Отклонено': 'Невозможно изменить данные пользователя'})
        return data