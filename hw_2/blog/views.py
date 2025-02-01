from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list_full_view(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list_full.html', {'articles': articles})

def article_detail_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})
