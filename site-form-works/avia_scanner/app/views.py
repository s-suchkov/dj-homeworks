import time
import random
import re
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    search = request.GET
    term = search['term']
    results = []
    cities = cache.get('key')
    if cities is None:
        value = City.objects.all()
        cache.set('key', value)
    for city in cities:
        if re.match(term.lower(), city.name.lower()):
            results.append(city.name)
    return JsonResponse(results, safe=False)



# def cache_choices():
#     value = []
#     if cache.get('key') is None:
#         for city in City.objects.all():
#             cache.set('key', city.name)
#             value.append(cache.get('key'))
#             print(cache.get('key'))
#     return value
#
# print(cache_choices())