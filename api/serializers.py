from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'email',
                  'first_name', 'last_name', 'bio']


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


# Кастомное поле для TitleSerializer
class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = CategorySerializer(value)
        return serializer.data


# Кастомное поле для TitleSerializer
class GenreField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = GenreSerializer(value)
        return serializer.data


class TitleSerializer(serializers.ModelSerializer):
    category = CategoryField(
        slug_field='slug', queryset=Category.objects.all()
    )
    genre = GenreField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )

    class Meta:
        model = Title
        fields = ('__all__')
