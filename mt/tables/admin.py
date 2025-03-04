from django.contrib import admin
from .models import Table

@admin.register(Table)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'seats', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('number',)
