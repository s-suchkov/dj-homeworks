from django.shortcuts import render
from .models import Profile, Article

def show_articles(request):
    tempate_name = 'articles.html'
    if request.user.is_authenticated:
        if request.user.profile.follows:
            return render(
                request,
                tempate_name,
                {'articles': Article.objects.all()}
            )
        else:
            return render(
                request,
                tempate_name,
                {'articles': Article.objects.all().filter(pay_follows=False)}
            )
    if not request.user.is_authenticated:
        return render(
            request,
            tempate_name,
            {'articles': Article.objects.all().filter(pay_follows=False)}
        )


def show_article(request, id):
    article = Article.objects.get(pk=id)
    return render(
        request,
        'article.html',
        {'article': article}
    )
article = Article.objects.filter()


# for profile in Profile.objects.all():
#     print(profile.follows)