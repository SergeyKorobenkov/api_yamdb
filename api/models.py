from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


def gen_slug(slug):
    new_slug = slugify(slug, allow_unicode=True)
    return new_slug


class Works(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_author",  verbose_name=_("Пользователь"))
    name = models.CharField(max_length=200,  verbose_name=_("Название"))
    rating = models.FloatField(
        default=0, null=True, blank=True, verbose_name=_("Рейтинг"))
    pub_date = models.DateTimeField(
        auto_now=True, verbose_name=_("Дата добавления"))

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = "Произведения"
        ordering = ["-pub_date"]

class Genre(models.Model):
    work = models.ManyToManyField(Works, related_name='genre', verbose_name=_("Жанр"))
    title = models.CharField(max_length=100,  verbose_name=_("Название"))
    slug = models.SlugField(max_length=150, unique=True,
                            verbose_name=_("Слаг"))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Сategory(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Название"))
    slug = models.SlugField(max_length=150, unique=True,
                            verbose_name=_("Слаг"))
    description = models.TextField(verbose_name=_("Описание"))
    work = models.ForeignKey(Works, on_delete=models.SET_NULL, blank=True,
                             null=True, related_name="category", verbose_name=_("Произведение"))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Vote(models.Model):
    value = models.SmallIntegerField(verbose_name=_("Оценка"))
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='work_vote', verbose_name=_("Пользователь"))
    work = models.ForeignKey(
        Works, on_delete=models.CASCADE, related_name='votes', verbose_name=_("Произведение"))
    voted_on = models.DateTimeField(
        auto_now=True, verbose_name=_("Дата оценки"))

    class Meta:
        unique_together = ('user', 'work')
        verbose_name = 'Оценка'
        verbose_name_plural = "Оценки"
