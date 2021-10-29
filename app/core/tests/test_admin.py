from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        self.cient  = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'adming@londonapp.de',
            password = 'password123'
        )
        self.client.force_login(self.admin_user)
        self.user  = get_user_model().objects.create_user(
            email = 'test@londonapp.dev',
            password = 'pw123',
            name = 'Test user full name'
        )
    
    def test_users_listed(self):
        """Test that users are listed on our page"""
        url = reverse('admin:core_user_changelist')
        # will use test client to do a http get on the url
        res = self.client.get(url)

        # check if response continas ceratin item
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    
    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse("admin:core_user_change",
            args=[self.user.id])
        #           reverse.args get appened here
        # it creates a url for us 
        # /admin/core/user/

        # import pdb; pdb.set_trace()
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """TEst that the create user page works"""

        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)