from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    num = {}
    for article in Article.objects.all():
        tag = article.scope_set.all().order_by('-is_main', 'tematik')
        num[article.id] = tag

    context = {
        'object_list': Article.objects.all(),
        'tass': num
    }

    return render(request, template, context)

