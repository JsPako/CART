from django.contrib.auth.views import LoginView
from .forms import UserAuthentication

class MyLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserAuthentication
