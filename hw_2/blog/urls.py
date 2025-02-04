from django.urls import path
from .views import article_list_full_view, article_detail_view

urlpatterns = [
    path('', article_list_full_view, name='article-list-full'),
    path('<int:article_id>/', article_detail_view, name='article-detail'),
]
