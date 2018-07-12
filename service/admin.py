from django.contrib import admin

from service.models import SEOMeta


@admin.register(SEOMeta)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('website', 'title')
