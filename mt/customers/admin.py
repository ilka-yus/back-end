from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    search_fields = ('id', 'name', 'phone')
