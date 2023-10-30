from django.contrib import admin
from django.utils.html import format_html
from body.models import Home_feild


# Register your models here.
admin.site.site_header  =  "My admin"  
admin.site.site_title  =  "My admin"
admin.site.index_title  =  "Welcome to My Admin"

class Home_f(admin.ModelAdmin):
    list_filter = ('title','idea')
    search_fields = ('idea',)
    list_display = ('id', 'title', 'title2', 'display_avatar', 'idea', 'details')

    def display_avatar(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.avatar.url)

    display_avatar.short_description = 'Avatar'

admin.site.register(Home_feild, Home_f)