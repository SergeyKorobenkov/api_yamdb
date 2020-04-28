from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Review(models.Model):
    score = models.SmallIntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(11)], verbose_name=_("Оценка"))
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='title_vote', verbose_name=_("Пользователь"))
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='votes', verbose_name=_("Произведение"))
    pub_date = models.DateTimeField(
        auto_now=True, verbose_name=_("Дата оценки"))
    text = models.TextField(verbose_name=_("Текст"))

    def __str__(self):
        return self.title.name


class Comment(models.Model):
    text = models.TextField(verbose_name=_("Текст"))
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_author")
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="vote_comment")


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
