from django.shortcuts import render
from .models import Article

def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    context = {
        'object_list': articles
    }
    return render(request, template, context)
