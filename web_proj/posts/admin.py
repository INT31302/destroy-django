from django.contrib import admin
from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'view_count',
        'created_at',
        'like_count',

    )
    search_fields = (
        'title',
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user',)
