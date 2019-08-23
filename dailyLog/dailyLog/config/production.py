# Settings that are unique to production go here
from .base import *

DEBUG = False

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

WSGI_APPLICATION = 'dailyLog.wsgi.application'

