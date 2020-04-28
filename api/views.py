from django.shortcuts import render
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.response import Response

from .models import *
from .models import Category, Genre, Title
from .permissions import IsAdminOrReadOnly
from .serializers import *
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer
from .utils import ObjectMixin


class ReviewViewSet(ObjectMixin, viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    model = Review
    serializer = ReviewSerializer


class CommentViewSet(ObjectMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    model = Comment
    serializer = CommentSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    lookup_field = 'slug'


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    lookup_field = 'slug'
