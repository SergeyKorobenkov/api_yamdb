from django.contrib import admin

from .models import *


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')
    empty_value_display = '-пусто-'

admin.site.register(Title, TitleAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	empty_value_display = '-пусто-'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, CategoryAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'score', 'text')
    empty_value_display = '-пусто-'

admin.site.register(Review, ReviewAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review',  'text')
    empty_value_display = '-пусто-'

admin.site.register(Comment, CommentAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',  'role')
    empty_value_display = '-пусто-'

admin.site.register(User, UserAdmin)
