from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()


def index(request):
    transition = request.GET['from-landing']
    if transition == 'original':
        counter_click['original'] += 1
    elif transition == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')


def landing(request):
    site = request.GET['ab-test-arg']
    if site == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    elif site == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')


def stats(request):
    if counter_click['test'] != 0 and counter_click['original'] != 0:
        return render_to_response('stats.html', context={
            'test_conversion': counter_click['test']/counter_show['test'],
            'original_conversion': counter_click['original']/counter_show['original'],
        })
    elif counter_click['test'] == 0:
        return render_to_response('stats.html', context={
            'test_conversion': 0,
            'original_conversion': counter_click['original'] / counter_show['original'],
        })
    elif counter_click['original'] == 0:
        return render_to_response('stats.html', context={
            'test_conversion': counter_click['test']/counter_show['test'],
            'original_conversion': 0,
        })
