from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import os
import urllib.request
import urllib.parse
from urllib.parse import urlencode
from app.settings import BUS_STATION_CSV
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse(bus_stations))



def bus_stations(request):
    page = request.GET.get('page')
    bus_station = []
    x = 0
    y = 0
    if page==None:
        page = 1
    with open(BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            bus_station.append({'Name' : line['Name'], 'Street' : line['Street'], 'District' : line['District']})
    p = Paginator(bus_station, 10)
    object = p.get_page(page)
    if object.has_next():
        query_arg_next = {'page': object.next_page_number()}
        query_arg_next = f'bus_stations?{urllib.parse.urlencode(query_arg_next)}'
    else:
        query_arg_next = None
    if object.has_previous():
        query_arg_prev = {'page': object.previous_page_number()}
        query_arg_prev = f'bus_stations?{urllib.parse.urlencode(query_arg_prev)}'
    else:
        query_arg_prev = None


    return render_to_response('index.html', context={
        'bus_stations': object,
        'current_page': page,
        'prev_page_url': query_arg_prev,
        'next_page_url': query_arg_next,
    })

