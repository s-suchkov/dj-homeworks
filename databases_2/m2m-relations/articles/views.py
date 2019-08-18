from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    context = {}
    context['object_list'] = Article.objects.all()
    # context['tags'] = []
    # for article in Article.objects.all():
    #     tag = article.scope_set.all().order_by('-is_main', 'tematik')
    #     context['tags'].append(tag)

    return render(request, template, context)

