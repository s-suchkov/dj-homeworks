import csv
import os
from django.core.management.base import BaseCommand
from app.models import Station, Route

class Command(BaseCommand):
    help = 'homework'

    def handle(self, *args, **options):
        file = 'moscow_bus_stations.csv'
        with open(file, 'r') as f_obj:
            reader = csv.DictReader(f_obj, delimiter=';')
            for line in reader:
                station = Station.objects.create(name=line['Name'], latitude=line['Latitude_WGS84'], longitude=line['Longitude_WGS84'])
                routes_num = line['RouteNumbers']
                for num in routes_num.split(';'):
                    route = Route.objects.create(name=num)
                    station.routes.add(route)
                # station.save()


