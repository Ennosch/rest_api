# from django
from unittest.mock import patch

#allow to call command in source code ?
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):
    
    def test_wait_for_db_rdy(self):
        '''Test waiting for db when db is available'''
        with patch('django.db.utils.ConnectionHandler.__getitem__' ) as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # raise OpError 5 time you call __getitem__
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)