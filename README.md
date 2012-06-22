A simple Django email backend that simply redirect email sent through the email 
framework to a specified recipients.

It always happened in development when you have to used production db to test 
that contain user's email, you end up sending email to real users from 
development system. It's embrassing and in unfortunate circumstances maybe will 
also cost your company a money.

## Installation

    pip install django-emailredirect

## Usage
Add this in your `settings.py`:-

    EMAIL_BACKEND = 'django_emailredirect.backends.EmailBackend'
    EMAIL_REDIRECT = ['redirect_to@example.com',]
