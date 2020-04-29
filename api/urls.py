from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *


router = DefaultRouter()
router.register('titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', 
                CommentViewSet, basename='comments')
router.register('titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
#router.register('users/(?P<username>\w+)', UserDetailViewSet, basename='user')   #ПОСМОТРЕТЬ И УБРАТЬ/РАСКОММЕНТИТЬ
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path("email/", get_confirmation_code, name="token_obtain_pair"),
    path('token/', get_jwt_token, name='token'),
]
