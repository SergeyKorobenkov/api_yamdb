from django.contrib import admin

# Register your models here.
from users.models import *
from reviews.models import *
from titles.models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'score', 'text')
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review',  'text')
    empty_value_display = '-пусто-'


admin.site.register(Comment, CommentAdmin)
