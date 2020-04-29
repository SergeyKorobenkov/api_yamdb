from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    bio = models.TextField(blank=True)
    username = models.CharField(max_length=100, blank=True, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class UserRole(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    role = models.CharField(
        max_length=9, choices=UserRole.choices, default=UserRole.USER)

    def __str__(self):
        return self.email


class Title(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    year = models.IntegerField(null=True, blank=True, verbose_name='Дата')
    description = models.CharField(max_length=100, null=True, 
                                blank=True, verbose_name='Описание')
    genre = models.ManyToManyField('Genre', related_name='title', blank=True)
    category = models.ForeignKey('Category', related_name='title', 
                                on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(default=None, null=True, 
                                blank=True, verbose_name='Рейтинг')

    def __str__(self):
        return self.name


class Review(models.Model):
    score = models.SmallIntegerField(validators=[MinValueValidator(1), 
                                MaxValueValidator(10)], verbose_name=_("Оценка"))
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='title_vote', verbose_name=_("Пользователь"))
    title = models.ForeignKey(Title, on_delete=models.CASCADE, 
                                related_name='votes', verbose_name=_("Произведение"))
    pub_date = models.DateTimeField(auto_now=True, verbose_name=_("Дата оценки"))
    text = models.TextField(verbose_name=_("Текст"))

    def __str__(self):
        return self.title.name


class Comment(models.Model):
    text = models.TextField(verbose_name=_("Текст"))
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                related_name="comment_author")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, 
                                related_name="vote_comment")


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Жанр')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name