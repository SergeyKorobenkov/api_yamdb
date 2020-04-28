from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('titles', views.TitleViewSet, basename='titles')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('genres', views.GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/', include(router.urls))
]
