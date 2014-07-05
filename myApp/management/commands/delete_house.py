__author__ = 'Hugh'

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option
from myApp.models import House
import sys


class Command(BaseCommand):
    args = '[address]'
    help = 'Deletes the given address from the database'

    option_list = BaseCommand.option_list + (
        make_option('--addr-contains',
                    action='store',
                    dest='address',
                    default=False,
                    help='deletes the house form the owner'),
    )

    def handle(self, *args, **options):

        """
            This function deletes the house attached to a user name based off of the given input
        """

        ## grab all the houses using add provided in command line as filter
        house = House.objects.filter(address__contains= options['address'])

        if not house:
            ## if that address does not exist throw error
            sys.stdout.write('address = [ %s ] does not exist \n' % options['address'])
            exit()

        ## loop over all of the filtered houses
        for h in house:
            ## print message
            sys.stdout.write('address = [ %s ] was removed \n' % h)
        ## delete houses from db
        house.delete()
