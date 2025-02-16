from django.contrib import admin
from .models import TodoList, Todo

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title')

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'due_date', 'status', 'todo_list')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')