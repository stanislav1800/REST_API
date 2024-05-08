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
    user_id = UsersSerializer()
    coords_id = CoordSerializer()
    level_id = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)
    # status = serializers.CharField()

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user_id', 'coords_id', 'level_id', 'images', 'status']


    def create(self, validated_data, **kwargs):
        user_data = validated_data.pop('user_id')
        coord_data = validated_data.pop('coords_id')
        level_data = validated_data.pop('level_id')
        images_data = validated_data.pop('images')

        user_id, created = User.objects.get_or_create(**user_data)
        coord_id = Coords.objects.create(**coord_data)
        level_id = Level.objects.create(**level_data)

        pereval = Pereval.objects.create(user_id=user_id, coords_id=coord_id, level_id=level_id, **validated_data)

        for image_data in images_data:
            Images.objects.create(**image_data, pereval=pereval)

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