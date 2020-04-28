from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()



class Title(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_author",  verbose_name=_("Пользователь"))
    name = models.CharField(max_length=200,  verbose_name=_("Название"))
    # genre = models.ManyToManyField(Genre, related_name='work', verbose_name=_("Жанр"))
    # category =  models.ForeignKey(Сategory, on_delete=models.SET_NULL,related_name="work", verbose_name=_("Категория"))
    rating = models.FloatField(default=0, null=True, blank=True, verbose_name=_("Рейтинг"))
    year = models.IntegerField(verbose_name=_("Год"))
    description = models.TextField(null=True, blank=True,verbose_name=_("Описание"))


class Rewiew(models.Model):
    score = models.SmallIntegerField(verbose_name=_("Оценка"))
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='title_vote', verbose_name=_("Пользователь"))
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='votes', verbose_name=_("Произведение"))
    pub_date = models.DateTimeField(
        auto_now=True, verbose_name=_("Дата оценки"))
    text = models.TextField( verbose_name=_("Текст"))


class Comment(models.Model):
    text = models.TextField(verbose_name=_("Текст"))
    created = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    review = models.ForeignKey(Rewiew, on_delete=models.CASCADE, related_name="vote_comment")

