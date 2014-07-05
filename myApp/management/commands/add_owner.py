__author__ = 'Hugh'

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from myApp.models import Owner
import sys


class Command(BaseCommand):
    args = '[owner]'
    help = 'adds a new owner'

    option_list = BaseCommand.option_list + (
        make_option('--name',
                    action='store',
                    dest='new_name',
                    default=False,
                    help='adds a new owner'),
    )

    def handle(self, *args, **options):

        """
            this function adds an owner to the database.
        """

        all_owners = Owner.objects.all()

        ## loop over all owners to check if owner already exists

        for name in all_owners:

            # check for name in database
            if options['new_name'] == str(name):
                ##name already exists
                raise CommandError('Owner name: "%s" already exists. Please enter another name' % options['new_name'])
                exit()

        ## add user to the database
        ## make new Owner object
        new_name = Owner()
        ## pass in new name
        new_name.name = options['new_name']
        ## save new name to database
        new_name.save()
        ## print success to the screen
        sys.stdout.write('Added owner: name = %s \n' % options['new_name'])


