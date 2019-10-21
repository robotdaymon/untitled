from django.core.management.base import BaseCommand
from testparcer.models import Parceline

class Command(BaseCommand):
    print('we are in xlssave command')

    def handle(self, *args, **options):
        # print(options['href'])
        import this

    def add_arguments(self, parser):
        parser.add_argument("-href", type=str, required=True)
