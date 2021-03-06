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

    def test_new_user_email_normalized(self):
        """Test email for new user is normalized"""
        email = "test@londonappdev.COM"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """TEst creating a new superuse"""
        user = get_user_model().objects.create_superuser(
            "test@londonapp.dev",
            "test123",)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)