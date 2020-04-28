from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(
    'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet)
router.register('titles/(?P<title_id>\d+)/reviews', ReviewViewSet)
router.register('titles', views.TitleViewSet, basename='titles')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('genres', views.GenreViewSet, basename='genres')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




urlpatterns += [
    path('v1/', include(router.urls))
]
