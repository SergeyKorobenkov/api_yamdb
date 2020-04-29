
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .filters import TitleFilter
from .models import Category, Comment, Genre, Review, Title, User
from .permissions import IsAdminorMe, IsAdminOrReadOnly
from .serializers import *
from .utils import ObjectMixin


@api_view(['POST'])
def get_confirmation_code(request):
    username = request.data.get('username')
    serializer = UserEmailSerializer(data=request.data)
    email = request.data.get('email')

    if serializer.is_valid():
        if username is not None:
            user = User.objects.filter(
                username=username) | User.objects.filter(email=email)
            if len(user) == 0:
                User.objects.create_user(username=username, email=email)
            else:
                return Response(serializer.errors, status=status.HTTP_418_IM_A_TEAPOT)
        user = get_object_or_404(User, email=email)
        confirmation_code = default_token_generator.make_token(user)
        mail_subject = 'Код подтверждения'
        message = f'Ваш код подтверждения: {confirmation_code}'
        send_mail(mail_subject, message, 'Yamdb.ru <admin@yamdb.ru>',
                  [email], fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_jwt_token(request):
    serializer = ConfirmationCodeSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.data.get('email')
        confirmation_code = serializer.data.get('confirmation_code')
        user = get_object_or_404(User, email=email)

        if default_token_generator.check_token(user, confirmation_code):
            token = AccessToken.for_user(user)
            return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
        return Response({'confirmation_code': 'Неверный код подтверждения'},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ObjectMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminorMe]
    model = User
    serializer = UserSerializer


# ПОСМОТРЕТЬ И УБРАТЬ/РАСКОМЕНТИТЬ
# class UserDetailViewSet(ObjectMixin, viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     model = User
#     serializer = UserSerializer


def AnyUser(request, username):
    user = get_object_or_404(User, username=username)
    return user


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
    filterset_class = TitleFilter


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
