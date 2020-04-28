from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    year = models.IntegerField(verbose_name='Дата')
    description = models.CharField(max_length=100, verbose_name='Описание')
    genre = models.ManyToManyField('Genre', related_name='title')
    category = models.ForeignKey(
        'Category', related_name='title', on_delete=models.SET_NULL, null=True)
    rating = models.FloatField(
        default=None, null=True, blank=True, verbose_name='Рейтинг')

    def __str__(self):
        return self.name


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
