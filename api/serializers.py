from rest_framework import serializers

from .models import Title, Category, Genre


class CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields = ('name', 'slug')
 
 
class GenreSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Genre
        fields = ('name', 'slug')
 
 
class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = CategorySerializer(value)
        return serializer.data
 
 
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