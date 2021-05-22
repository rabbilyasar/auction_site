from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LoginTest(TestCase):
    def setUp(self) -> None:
        self.login_url = reverse('users:login')
        self.credentials = {
            'email': 'test@user.com',
            'password': 'testpass123'
        }
        self.user = get_user_model().objects.create_user(**self.credentials)

    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    def test_login_success(self):
        self.client.post(self.login_url, self.credentials, format='text/html')
        user = get_user_model().objects.get(email=self.credentials['email'])
        self.assertTrue(user.is_authenticated)
