from django.core.management.base import BaseCommand

from main.models import Location


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('cities.txt', 'r') as f:
            all_locations = list(f.read().split('\n'))

        for location in all_locations:
            loc, created = Location.objects.get_or_create(name=location)