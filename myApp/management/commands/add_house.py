__author__ = 'Hugh'

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option
from myApp.models import Owner, House
import sys

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
                    dest='owner_name',
                    default=False,
                    help='destination owner')
    )

    def handle(self, *args, **options):

        """
            This function adds a house to a provided user.
            If the user does not exist, it creates the user and prints that the user was updated
            and then prints out the address and user
        """

        ## check for the owner in the database
        try:
            Owner.objects.get(name=options['owner_name'])
        except ObjectDoesNotExist:
            ## new owner does not exist
            ##create new owner object
            new_owner = Owner()
            ##assign name to new owner
            new_owner.name = options['owner_name']
            ##save new owner to database
            new_owner.save()
            self.stdout.write('Added Owner: name =  %s' % options['owner_name'])


        self.add_owner(options['owner_name'], options['new_house'])

    def add_owner(self, owner, house):
        ## grab owner from database
        owner = Owner.objects.get(name=owner)
        #create new house
        new_house = House()
        #assign address to house object
        new_house.address = house
        #assign owner to house object
        new_house.owner = owner
        #save the object to the database
        new_house.save()
        #message fo output
        sys.stdout.write('Added house: address =  %s' % house)
        sys.stdout.write('Owner =  %s \n' % owner)














