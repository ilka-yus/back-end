from django.urls import path
from .views import movie_list_full_view, movie_detail_view

urlpatterns = [
    path('movies/', movie_list_full_view, name='movie-list-full'),
    path('movies/<int:movie_id>/', movie_detail_view, name='movie-detail'),
]
