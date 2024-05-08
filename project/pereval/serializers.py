from .models import *
from rest_framework import serializers


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


class PerevalSerializer(serializers.ModelSerializer):
    print('Зашол')
    user = UsersSerializer()
    coord = CoordSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)
    status = serializers.CharField()

    class Meta:
        model = Pereval
        depth = 1
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level', 'images', 'status']


    def create(self, validated_data, **kwargs):
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coord')
        level_data = validated_data.pop('level')
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