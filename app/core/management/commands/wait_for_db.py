import time
#check if db model is available
from django.db import connection, connections
from django.db.utils import OperationalError
# class to build on to create custom command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    '''Django cmd to pause execution till database is available'''
    def handle(self, *args, **options):
        """check if available. if so clean"""
        self.stdout.write('Waiting for database ...')
        db_conn = None
        while not db_conn:
            try:
                # check if connection is available
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('database unavailable waiting 1 sec')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('database available!'))