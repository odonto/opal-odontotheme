"""
Standalone test runner for odontotheme plugin
"""
import os
import sys
from django.conf import settings

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   ROOT_URLCONF='opal.urls',
                   STATIC_URL='/assets/',
                   COMPRESS_ROOT='/tmp/',
                   DATE_FORMAT = 'd/m/Y',
                   DATE_INPUT_FORMATS = ['%d/%m/%Y'],
                   DATETIME_FORMAT = 'd/m/Y H:i:s',
                   DATETIME_INPUT_FORMATS = ['%d/%m/%Y %H:%M:%S'],
                   TIME_FORMAT = "H:i:s",
                   MIDDLEWARE_CLASSES = (
                       'django.middleware.common.CommonMiddleware',
                       'django.contrib.sessions.middleware.SessionMiddleware',
                       'opal.middleware.AngularCSRFRename',
                       'django.middleware.csrf.CsrfViewMiddleware',
                       'django.contrib.auth.middleware.AuthenticationMiddleware',
                       'django.contrib.messages.middleware.MessageMiddleware',
                       'opal.middleware.DjangoReversionWorkaround',
                       'reversion.middleware.RevisionMiddleware',
                       'axes.middleware.FailedLoginMiddleware',
                   ),
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.staticfiles',
                                   'django.contrib.admin',
                                   'compressor',
                                   'opal',
                                   'odontotheme',))

import django
django.setup()

from opal.core import application

class Application(application.OpalApplication):
    pass

try:
    sys.argv.remove('--failfast')
    failfast = True
except ValueError:
    failfast = False


from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1, failfast=failfast)
if len(sys.argv) == 2:
    failures = test_runner.run_tests([sys.argv[-1], ])
else:
    failures = test_runner.run_tests(['odontotheme', ])
if failures:
    sys.exit(failures)