from .serializers import *
from .models import *
from .utils import ObjectMixin

from rest_framework import viewsets

class ReviewViewSet(ObjectMixin,viewsets.ModelViewSet):
    queryset = Rewiew.objects.all()
    serializer_class = RewiewSerializer
    model = Rewiew
    serializer = RewiewSerializer


class CommentViewSet(ObjectMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    model = Comment
    serializer = CommentSerializer
