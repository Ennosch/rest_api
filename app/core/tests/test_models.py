from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_sucessfull(self):
        """Test Create with a new user with an email is sucessfull"""
        email = "test@londonappdev.com"
        password = "Testpass123"
        # import pdb; pdb.set_trace()
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
            # username = 'testuser'
        )
        # import pdb; pdb.set_trace()
        self.assertEqual(user.email, email)
        self.assertEqual(user.email  , email)
        self.assertTrue(user.check_password(password))