
import unittest

from django.conf import settings

# Can't find a way to test yet since when running under django
# tests, django change the email backend to locmem internally
# so custom email backend will never used.

settings.configure(**{
    'EMAIL_BACKEND': 'django_emailredirect.backends.EmailBackend',
    'EMAIL_REDIRECT': ['redirect@example.com'],
})
from django.core.mail import send_mail

class TestEmailRedirect(unittest.TestCase):
    def test_redirect_email(self):
        send_mail('Test redirect', 'Testing', 'from@example.com', ['to@example.com'])
