from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Avg
from .models import *
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


class ObjectMixin():
    model = None
    serializer = None

    def list(self, request, title_id=None, review_id=None):
        if review_id:
            obj = self.model.objects.filter(review=review_id)
        else:
            obj = self.model.objects.filter(title__id=title_id)

        page = self.paginate_queryset(obj)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer(obj, many=True)
        return Response(serializer.data)

    def create(self, request, title_id=None, review_id=None):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            title = Title.objects.get(id=title_id)
            if review_id:
                review = Review.objects.get(id=review_id)
                serializer.save(author=request.user, review=review)
            else:
                serializer.save(author=request.user, title=title)
                rat = Rewiew.objects.filter(
                    title=title).aggregate(Avg('score'))['score__avg']
                rat = round(rat, 1)
                title.rating = rat
                title.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, title_id=None, review_id=None, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, title_id=None, review_id=None, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, title_id=None, review_id=None, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
