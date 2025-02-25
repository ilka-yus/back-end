from django.contrib import admin
from .models import Thread, Post

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id', 'title')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'picture', 'description', 'author', 'thread')
    search_fields = ('id', 'title', 'author')