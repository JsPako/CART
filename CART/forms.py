from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class UserAuthentication(AuthenticationForm):
    error_messages = {
        'invalid_login': _("Username or password is incorrect. Please check your details and try again."),
        'inactive': _("This account is inactive."),
    }

