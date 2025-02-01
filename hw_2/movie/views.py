from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_list_full_view(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list_full.html', {'movies': movies})

def movie_detail_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie/movie_detail.html', {'movie': movie})
