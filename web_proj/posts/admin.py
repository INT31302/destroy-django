from django.contrib import admin
from .models import Post, Like, Comment
from django.contrib.auth import get_user_model
User = get_user_model()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'view_count',
        'created_at',
        'like_count',
        'author'

    )
    search_fields = (
        'title',
        'post__author',
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'writer',
        'comment',
        'text',
        'created_date'
    )
