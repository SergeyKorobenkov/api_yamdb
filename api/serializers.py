from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'гusername', 'role', 'email', 'first_name', 'last_name', 'bio']


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


