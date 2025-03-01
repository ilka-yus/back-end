from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'due_date', 'status', 'user')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'status')