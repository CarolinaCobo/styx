from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'post_title',
        'post_author',
        'post_date_posted',
    )

    ordering = ('-post_date_posted',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment_title',
        'comment_author',
        'comment_date_posted',
    )

    ordering = ('-comment_date_posted',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
