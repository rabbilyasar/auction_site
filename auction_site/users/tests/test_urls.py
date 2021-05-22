from django.test import TestCase
from django.urls import reverse, resolve
from users.views import SignUpView, LoginView
from django.contrib.auth import views as auth_views

class UrlsTest(TestCase):

    def test_signup_url_is_resolved(self):
        url = reverse('users:signup')
        self.assertEqual(resolve(url).func.__name__, SignUpView.as_view().__name__)

    def test_login_url_is_resolved(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func.__name__, LoginView.as_view().__name__)

    def test_logout_url_is_resolved(self):
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func, auth_views.logout_then_login)