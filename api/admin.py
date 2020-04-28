from django.contrib import admin
from .models import *


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')
    empty_value_display = '-пусто-'

admin.site.register(Title, TitleAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'score', 'text')
    empty_value_display = '-пусто-'

admin.site.register(Review, ReviewAdmin)
