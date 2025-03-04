from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'table', 'date', 'status')
    list_filter = ('date', 'status')
    search_field = ('customer__name', 'table__number')
