from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from users.forms import LoginForm

from .views import SignUpView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name="login.html",
        authentication_form=LoginForm
    ), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
]
