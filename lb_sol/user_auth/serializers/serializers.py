from rest_framework import serializers

from user_auth.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('email', 'password')
