from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from myApp.models import Owner, House

class Command(BaseCommand):
    args = '[house], [owner]'
    help = 'adds a new house to owner'
    option_list = BaseCommand.option_list + (
        make_option('--house',
            action='store',
            dest='new_house',
            default=False,
            help='adds a new house'),
        make_option('--name',
            action='store',
            dest='new_name',
            default=False,
            help = 'destination owner')
        )


    def handle(self, *args, **options):

        for data in args:
            print data

        print options['new_house']


