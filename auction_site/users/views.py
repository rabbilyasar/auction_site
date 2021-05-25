from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

User = get_user_model()


class SignUpView(SuccessMessageMixin, CreateView):
    """Registers a new user
    """
    model = User
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_message = "You have been registered succesfully"

    def get_success_url(self) -> str:
        return reverse('users:login')


class LoginView(auth_views.LoginView):
    """Logs in a new user using django's default loginview

    Args:
        auth_views ([type]): [description]
    """
    template_name = 'login.html'
