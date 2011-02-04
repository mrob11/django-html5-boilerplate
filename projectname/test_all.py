#!/usr/bin/python

import os, sys, commands

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

for app in settings.INSTALLED_APPS:
    i = app.rfind('.')
    if i == -1:
        m, a = app, None
    else:
        m, a = app[:i], app[i+1:]
    try:
        if a is None:
            mod = __import__(m, {}, {}, [])
        else:
            mod = getattr(__import__(m, {}, {}, [a]), a)
    except ImportError, e:
        raise ImproperlyConfigured, 'ImportError %s: %s' % (app, e.args[0])
    if os.path.exists(os.path.join(os.path.dirname(mod.__file__),
            'tests/settings.py')):
        print "Running tests for %s..." % mod.__name__,
        status, output =  commands.getstatusoutput(
            './manage.py test tests --settings=%s.tests.settings' %
            mod.__name__)
        if status == 0:
            print "OK"
            print output.split('\n')[2] # display "Ran n tests in n sec"
        else:
            print "FAILED"
            print output

print 'Running remaining tests...'
os.system('./manage.py test')
