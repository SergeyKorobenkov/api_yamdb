from django.urls import path, include
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, get_confirmation_code, get_jwt_token, AnyUser


router = DefaultRouter()
router.register('api/v1/users', UserViewSet)


urlpatterns = [
        path('', include(router.urls)),
        path("api/v1/auth/email", get_confirmation_code, name="token_obtain_pair"),
        path('api/v1/auth/token', get_jwt_token, name='token'),
    ]