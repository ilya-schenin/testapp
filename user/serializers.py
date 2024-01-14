from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        index = validated_data['email'].index('@')
        user = UserModel.objects.create_user(
            username=validated_data['email'][:index],
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data['phone'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "email", "password", "phone")