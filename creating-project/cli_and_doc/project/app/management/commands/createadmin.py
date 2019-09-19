from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('password')
    def handle(self, *args, **options):
        User.objects.create_superuser(username=options['name'], password=options['password'], email=None)