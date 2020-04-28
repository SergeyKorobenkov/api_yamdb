from django.contrib import admin

from api.models import User

#class UserAdmin(admin.ModelAdmin):
    #list_display = ('pk','text','pub_date','author')
    #search_fields = ('text',)
    #list_filter = ('pub_date',)
    #empty_value_display = '-пусто-'

admin.site.register(User)