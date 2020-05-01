from django.contrib import admin

# Register your models here.
from users.models import *
from reviews.models import *
from titles.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',  'role')
    empty_value_display = '-пусто-'

admin.site.register(User, UserAdmin)