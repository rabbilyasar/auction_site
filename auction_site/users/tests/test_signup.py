from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from users.forms import CustomUserCreationForm


class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.email = 'testuser@mail.com'
        self.password = '123safe123'

    def test_signup_view_name(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='signup.html')

    def test_signup_form(self):
        form = CustomUserCreationForm(data = {
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
        })
        self.assertTrue(form.is_valid())

    def test_registration_with_success(self):
        response = self.client.post(reverse('users:signup'), data = {
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
        })
        user = get_user_model().objects.last()
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)