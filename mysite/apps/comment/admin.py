from django.contrib import admin
from comment.models import Comment, Message

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'body', 'create_date','belong']

@admin.register(Message)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'create_date','belong']
