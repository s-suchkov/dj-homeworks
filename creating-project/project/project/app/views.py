from django.shortcuts import render
from .models import Station, Route
# Create your views here.
def station(request):
    template = 'stations.html'
    context = {
        'routes': Route.objects.all(),
    }
    if request.GET:
        get_route = request.GET['route']
        stations = Station.objects.all().filter(routes__name=get_route)
        print(stations)
        x1 = stations.first().longitude
        x2 = stations.last().longitude
        x = (float(x1) + float(x2))/2
        y1 = stations.first().latitude
        y2 = stations.last().latitude
        y = (float(y1)+float(y2))/2
        center = {
            'x':x,
            'y':y
        }
        context = {
            'routes': Route.objects.all(),
            'stations': stations,
            'center':center
        }

    result = render(request, template, context)
    return result

