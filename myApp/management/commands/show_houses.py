__author__ = 'Hugh'
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option
from myApp.models import House, Owner
import sys



class Command(BaseCommand):
    args = '[owner]'
    help = 'displays all houses'
    option_list = BaseCommand.option_list + (
        make_option('--owner',
                    action='store',
                    dest='owner',
                    default=False,
                    help='filters houses by owner'),
    )

    def handle(self, *args, **options):

        """
            This function shows all of the houses and their owners in the database.
            If the option --owner is given it shows the house and owner of the given input
        """

        if options['owner']:
            ## check for the owner in the database
            try:
                Owner.objects.get(name=options['owner'])

            except ObjectDoesNotExist:
                sys.stdout.write('Name = [ %s ] does not exist \n' % options['owner'])
                exit()

            house = House.objects.get(owner = owner.id)
            sys.stdout.write('address = [ %s ] ' % house.address)
            sys.stdout.write('owner =  [ %s ] \n' % house.owner)
        else:
            ## grab all houses form the database
            houses = House.objects.all()
            #loop over all houses
            for h in houses:
                ## print houses to the screen
                sys.stdout.write('address = [ %s ] ' % h.address)
                sys.stdout.write('owner =  [ %s ] \n' % h.owner)


