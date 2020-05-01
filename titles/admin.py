from django.contrib import admin

from users.models import *
from reviews.models import *
from titles.models import *


# please read the message_for_reviewer in BASE_DIR
class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')
    empty_value_display = '-пусто-'

admin.site.register(Title, TitleAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	empty_value_display = '-пусто-'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, CategoryAdmin)



